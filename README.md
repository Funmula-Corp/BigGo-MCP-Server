# 🔍 BigGo MCP Server
[![smithery badge](https://smithery.ai/badge/@Funmula-Corp/BigGo-MCP-Server)](https://smithery.ai/server/@Funmula-Corp/BigGo-MCP-Server)

A Model Context Protocol (MCP) server that provides product search, price history tracking, and specification search capabilities.

## ✨ Features

### 🛍️ Product Search
Search for products across multiple e-commerce platforms with natural language queries.

**Example Prompts:**
```
Find me iPhone 15 Pro on Shopee
```
```
Look for Nike running shoes
```

### 📈 Price History Tracking
Track product price history in two ways:
- Direct URL tracking
- History ID tracking (obtained from product search results)

**Example Prompts:**
```
Show me the price history of this product: https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=13660781
```
```
Find me the price history of IPhone 15 Pro at Shopee?
```

### 📐 Product Specification Search
Search for products based on specific technical specifications using Elasticsearch.

**Example Prompts:**
```
Find me refrigerators with the highest energy efficiency rating
```
```
Search for diving watches that weigh around 120g
```
```
Show me Japanese air conditioners with heating capability and low noise levels
```

## 🛠️ Available Tools

### 🛍️ Product Search Tools
- `product_search`
  - Product search with biggo search api

### 📈 Price History Tools
- `price_history_graph`
  - Link that visualizes product price history
- `price_history_with_history_id`
  - Uses history IDs from product search results
  - Typical tool workflow: Search product -> Get history ID -> Track prices
- `price_history_with_url`
  - Tracks price history using product URLs

### 📐 Specification Search Tools
- `spec_indexes`
  - Lists available Elasticsearch indexes for product specifications
- `spec_mapping`
  - Shows Elasticsearch index mapping with example documents
- `spec_search`
  - Advanced specification-based product search

### 🧰 Utility Tools
- `get_current_region`
  - Get the current region setting

## ⚙️ Installation

### 📋 Prerequisites
> PyPi package link: [biggo-mcp-server](https://pypi.org/project/biggo-mcp-server/)
1. Python 3.13 or higher
2. [uv package manager](https://docs.astral.sh/uv/)
3. BigGo API credentials (client ID and secret) for specification search. Available at [BigGo Account](https://account.biggo.com/setting/token)

### Installing via Smithery

To install BigGo MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@Funmula-Corp/BigGo-MCP-Server):

```bash
npx -y @smithery/cli install @Funmula-Corp/BigGo-MCP-Server --client claude
```

### 💻 From Local Project
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
        "biggo-mcp-server",
        "--client-id",
        "YOUR_CLIENT_ID",
        "--client-secret",
        "YOUR_CLIENT_SECRET"
      ],
      "enabled": true
    }
  }
}
```

### 📦 From Published Package
> For specific version use `biggo-mcp-server@VERSION`, ex: `biggo-mcp-server@0.1.1`
```json
{
  "mcpServers": {
    "biggo-mcp-server": {
      "command": "uvx",
      "args": [
        "biggo-mcp-server",
        "--client-id",
        "YOUR_CLIENT_ID",
        "--client-secret",
        "YOUR_CLIENT_SECRET"
      ],
      "enabled": true
    }
  }
}
```

## 🔧 Configuration Arguments

| Variable              | Description                       | Default                                    | Choices                                    |
| --------------------- | --------------------------------- | ------------------------------------------ | ------------------------------------------ |
| `--region`            | Region for product search         | TW                                         | US, TW, JP, HK, SG, MY, IN, PH, TH, VN, ID |
| `--client-id`         | Client ID                         | None                                       | Required for specification search          |
| `--client-secret`     | Client Secret                     | None                                       | Required for specification search          |
| `--log-level`         | Log level                         | INFO                                       | DEBUG, INFO, WARNING, ERROR, CRITICAL      |
| `--es-proxy-url`      | Elasticsearch proxy URL           | https://api.biggo.com/api/v1/mcp-es-proxy/ | Any valid URL                              |
| `--es-verify-certs`   | Verify Elasticsearch certificates | True                                       | True, False                                |
| `--auth-token-url`    | Auth token URL                    | https://api.biggo.com/auth/v1/token        | Any valid URL                              |
| `--auth-verify-certs` | Verify Auth certificates          | True                                       | True, False                                |

## 👨‍💻 Development

### 🚀 Setup
1. Install [uv](https://docs.astral.sh/uv/) package manager
2. Install dependencies:
   ```
   uv sync
   ```

### 🧪 Testing and Development
1. Run with MCP Inspector:
   ```
   npx @modelcontextprotocol/inspector uv run biggo-mcp-server
   ```

2. Run tests:
   ```
   uv run --group test pytest
   ```

### 📦 Project Architecture
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

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
