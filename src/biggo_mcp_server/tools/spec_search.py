from typing import Annotated
from mcp.server.fastmcp import Context
from pydantic import Field


async def spec_indexes(
    ctx: Context,
) -> Annotated[str, Field(description="List of Elasticsearch indexes")]:
    """Elasticsearch Indexes for Product Specification"""
    return "Not implemented"


async def spec_mapping(
    ctx: Context,
    index: Annotated[str,
                     Field(description="""
                          Elasticsearch index
                          Steps to obtain this argument.
                          1. Use 'spec_indexes' tool to get the list of indexes
                          2. Choose the most relevant index
                          """)],
) -> Annotated[str, Field(description="Elasticsearch Mappings")]:
    """Elasticsearch Mapping For Product Specification """
    return "Not implemented"


async def spec_search(
    ctx: Context,
    index: Annotated[str,
                     Field(description="""
                          Elasticsearch index
                          Steps to obtain this argument.
                          1. Use 'spec_indexes' tool to get the list of indexes
                          2. Choose the most relevant index
                          """)],
    query: Annotated[str,
                     Field(description="""
                          Elasticsearch query, no need to include the `query` field.
                          Steps to know what to query:
                          1. Use 'spec_indexes' tool to get the list of indexes
                          2. Choose the most relevant index
                          3. Use 'spec_mapping' tool to get the mapping of the index
                          4. Use this tool to query the index
                          5. If the mapping has 'region' related fields, 
                             use 'get_current_region' tool to get the current region
                             and apply it in the query. Regions are in lowercase.
                          """)],
) -> str:
    """Product Specification Search"""
    return "Not implemented"
