from biggo_mcp_server.types.api_ret.product_search import ListItem, ProductSearchAPIRet
from biggo_mcp_server.types.responses import ProductSearchToolResponse, SpecSearchToolResponse


def test_product_search_resp():
    resp = ProductSearchToolResponse(product_search_result=ProductSearchAPIRet(
        list=[]))

    assert resp.reason is not None

    resp = ProductSearchToolResponse(product_search_result=ProductSearchAPIRet(
        list=[
            ListItem(
                oid="123",
                title="test",
                price=100,
                purl="https://www.test.com",
            )
        ]))

    assert resp.reason is None


def test_spec_search_resp():
    resp = SpecSearchToolResponse(hits=[])

    assert resp.reason is not None

    resp = SpecSearchToolResponse(hits=[{"some": "data"}])

    assert resp.reason is None
