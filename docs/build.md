# Build Documentation
Documentation for local development and installation.

## Development
### Prerequisites
1. Python >= 3.10
2. [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)

### Install dependencies
```bash
uv sync
```

### Start with MCP inspector
```bash
npx @modelcontextprotocol/inspector uv run BigGo-MCP-Server
```

### Test
Copy `.env.example` to `test/.env.test` or `./.env.test`  
Update the credentials in `test/.env.test` or `./.env.test` with your BigGo API credentials
```bash
uv run --group test pytest
```

### Use the Alive tool
Sends a request to check if the SSE server is alive
```bash
uvx --from BigGo-MCP-Server BigGo-MCP-Server-Alive-Checker
```

## Install From Local Project
Use absolute path for `--directory` argument.
```json
{
  "mcpServers": {
    "biggo-mcp-server": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/biggo-mcp-server",
        "BigGo-MCP-Server",
      ],
      "env": {
        "BIGGO_MCP_SERVER_CLIENT_ID": "YOUR_CLIENT_ID",
        "BIGGO_MCP_SERVER_CLIENT_SECRET": "YOUR_CLIENT_SECRET",
        "BIGGO_MCP_SERVER_REGION": "YOUR_REGION"
      }
    }
  }
}
```

### Complete Environment Variables
| Variable                              | Description                          | Default                                      | Choices                                    |
| ------------------------------------- | ------------------------------------ | -------------------------------------------- | ------------------------------------------ |
| `BIGGO_MCP_SERVER_REGION`             | Region for product search            | TW                                           | US, TW, JP, HK, SG, MY, IN, PH, TH, VN, ID |
| `BIGGO_MCP_SERVER_CLIENT_ID`          | Client ID                            | None                                         | Required for specification search          |
| `BIGGO_MCP_SERVER_CLIENT_SECRET`      | Client Secret                        | None                                         | Required for specification search          |
| `BIGGO_MCP_SERVER_LOG_LEVEL`          | Log level                            | INFO                                         | DEBUG, INFO, WARNING, ERROR, CRITICAL      |
| `BIGGO_MCP_SERVER_ES_PROXY_URL`       | Elasticsearch proxy URL              | `https://api.biggo.com/api/v1/mcp-es-proxy/` |
| `BIGGO_MCP_SERVER_ES_VERIFY_CERTS`    | Verify Elasticsearch certificates    | True                                         | True, False                                |
| `BIGGO_MCP_SERVER_AUTH_TOKEN_URL`     | Auth token URL                       | `https://api.biggo.com/auth/v1/token`        |
| `BIGGO_MCP_SERVER_AUTH_VERIFY_CERTS`  | Verify Auth token URL certificates   | True                                         | True, False                                |
| `BIGGO_MCP_SERVER_SSE_PORT`           | Port for SSE server                  | 9876                                         | Any available port number                  |
| `BIGGO_MCP_SERVER_SERVER_TYPE`        | Server Type                          | stdio                                        | stdio, sse                                 |
| `BIGGO_MCP_SERVER_SHORT_URL_ENDPOINT` | Endpoint for short URL generator API | None                                         |                                            |

## Project Architecture
```
src/
└── biggo_mcp_server/
    ├── __init__.py         # MCP Server Entrypoint
    ├── lib/
    │   ...
    │   ├── server.py       # Server class      
    │   └── server_setup.py # Server initialization (load tools..etc)
    ├── services/           # Tool logic
    ├── tools/              # Tool entrypoint
    └── types/
        ├── api_ret/        # API responses
        ...
        ├── responses.py    # Tool responses
        └── setting.py      # Server setting
```

## Publishing
Publishing is done automatically with GitHub Actions when a new release is created. 
1. Create a new release in the GitHub Releases page
2. GitHub Actions will build the project and push the new version to PyPI
3. Package version will be the release tag, ex: `v0.1.1`
