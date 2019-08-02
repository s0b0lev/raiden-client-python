from raiden_client.plugins.v1.tokens import TokensPlugin


def test_tokens() -> None:
    request = TokensPlugin()
    assert request.endpoint == "/tokens"
    assert request.method == "get"
    assert not request.payload()


def test_tokens_in_tokens_network() -> None:
    request = TokensPlugin(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert request.endpoint == f"/tokens/{request.token_address}"
    assert request.method == "get"
    assert not request.payload()