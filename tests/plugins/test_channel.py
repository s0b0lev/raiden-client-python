from raiden_client.plugins.v1.channel import ChannelPlugin


def test_channel() -> None:
    channel = ChannelPlugin(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
    )
    assert channel.endpoint == f"/channels/{channel.token_address}/{channel.partner_address}"
    assert channel.method == "get"
    assert not channel.payload()
