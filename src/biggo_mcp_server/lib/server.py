import os
import signal
from asyncio import CancelledError, Event, Task, create_task
from logging import getLogger
from typing import Any

from mcp.server.fastmcp import FastMCP

from ..types.setting import BigGoMCPSetting

logger = getLogger(__name__)


class BigGoMCPServer(FastMCP):
    def __init__(self, setting: BigGoMCPSetting):
        super().__init__("BigGo MCP Server")
        self._biggo_setting = setting
        self.settings.port = setting.sse_port
        self._end_event: Event = Event()
        self._bg: list[Task[Any]] = []

    @property
    def biggo_setting(self) -> BigGoMCPSetting:
        return self._biggo_setting

    async def _run_stdio_async(self) -> None:
        logger.info("Start stdio BigGo MCP Server")
        try:
            return await self.run_stdio_async()
        except (KeyboardInterrupt, CancelledError) as ex:
            logger.warning(ex)
        except Exception:
            logger.exception("[stdio] somthing is wrong")
        finally:
            self._end_event.set()

    async def _run_sse_async(self) -> None:
        logger.info("Start SSE BigGo MCP Server")
        try:
            await super().run_sse_async()
        except (KeyboardInterrupt, CancelledError) as ex:
            logger.warning(ex)
        except Exception:
            logger.exception("[SSE] somthing is wrong")
        finally:
            self._end_event.set()

    async def start(self):
        if self.biggo_setting.server_type == "sse":
            sse_bg = create_task(self._run_sse_async(), name="sse-bg")
            self._bg.append(sse_bg)
        else:
            stdio_bg = create_task(self._run_stdio_async(), name="stdio-bg")
            self._bg.append(stdio_bg)

    async def _cleanup(self):
        for task in self._bg:
            logger.info("cancel task: %s", task.get_name())
            task.cancel()

    async def wait_finish(self):
        await self._end_event.wait()
        logger.info("Server shutting down")
        await self._cleanup()
        logger.info("Server shutdown complete")
        os.kill(os.getpid(), getattr(signal, "SIGKILL", signal.SIGTERM))
