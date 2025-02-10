from logging import getLogger
from typing import Annotated, Literal
from mcp.server.fastmcp import FastMCP
from pydantic import Field
import requests
from .lib.log import setup_logging
from .types.setting import BigGoMCPSetting
from .lib.price_history import get_price_history, get_price_history_with_url
from .types.product_search_ret import ProductSearchAPIRet
from .lib.utils import get_nindex_oid

logger = getLogger(__name__)

server = FastMCP("BigGo MCP Server")
setting = BigGoMCPSetting()
setup_logging(setting.log_level)


@server.tool()
def product_search(
    query: Annotated[
        str, Field(description="Search query", examples=["iphone", "護唇膏"])]
) -> str:
    """Product Search"""

    logger.info("product search, query: %s", query)

    url = f"https://biggo.com.tw/api/v1/spa/search/{query}/product"
    logger.debug("product search, url: %s", url)

    resp = requests.get(url)
    if resp.status_code >= 400:
        err_msg = f"product search api error: {resp.text}"
        logger.error(err_msg)
        raise ValueError(err_msg)

    # clean data
    original_length = len(resp.text)
    cleaned_data = ProductSearchAPIRet.model_validate_json(resp.text)
    result = cleaned_data.model_dump_json(exclude_none=True)

    logger.info("Original length: %s, Cleaned length: %s", original_length,
                len(result))

    return result


@server.tool()
def price_history_graph(
    history_id: Annotated[
        str,
        Field(description="""
              Product History ID
              Here are a few steps to obtain this argument.
              1. Use 'product_search' tool to retrive a list of products
              2. Find the most relevant product.
              3. The product should have a field called 'history_id', use it as the value for this argument
              """,
              examples=[
                  "tw_pmall_rakuten-nwdsl_6MONJRBOO", "tw_pec_senao-1363332"
              ])],
    language: Annotated[Literal["tw", "en"],
                        Field(description="Timeline label language")],
) -> str:
    """Link that visualizes product price history"""

    logger.info("price history graph, history_id: %s, language: %s", history_id,
                language)

    item_info = get_nindex_oid(history_id)
    url = f"https://imbot-dev.biggo.dev/chart?nindex={item_info.nindex}&oid={item_info.oid}&lang={language}"

    return f"""<PriceHistoryGraph> ![Price History Graph]({url}) </PriceHistoryGraph>"""


@server.tool()
def price_history_with_history_id(
    history_id: Annotated[
        str,
        Field(description="""
              Product History ID
              Here are a few steps to obtain this argument.
              1. Use 'product_search' tool to retrive a list of products
              2. Find the most relevant product.
              3. The product should have a field called 'history_id', use it as the value for this argument
              """,
              examples=[
                  "tw_pmall_rakuten-nwdsl_6MONJRBOO", "tw_pec_senao-1363332"
              ])],
    days: Annotated[Literal["90", "80", "365", "730"],
                    Field(description="History range")],
) -> str:
    """Product Price History With History ID"""

    logger.info("price history with history id, history_id: %s, days: %s",
                history_id, days)
    resp = get_price_history(history_id=history_id, days=int(days))
    if resp is None:
        return "No price history found"
    return resp.model_dump_json(exclude_none=True)


@server.tool()
def price_history_with_url(
    days: Annotated[Literal["90", "80", "365", "730"],
                    Field(description="History range")],
    url: Annotated[str, Field(description="Product URL")],
) -> str:
    """Product Price History With URL"""

    logger.info("price history with url, url: %s, days: %s", url, days)
    resp = get_price_history_with_url(days=int(days), url=url)
    if resp is None:
        return "No price history found"
    return resp.model_dump_json(exclude_none=True)
