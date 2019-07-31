from raidenpy.endpoints.pending_transfers import PendingTransfersRequest


def test_pending_transfers():
    request = PendingTransfersRequest()
    assert request.endpoint == "/address"
    assert request.method == "get"
    assert not request.payload()


def test_pending_transfers_specified_token():
    token_address = "0x123"
    request = PendingTransfersRequest(token_address=token_address)
    assert request.endpoint == f"/address/{token_address}"


def test_pending_transfers_specified_token_channel():
    token_address = "0x123"
    partner_address = "0x321"
    request = PendingTransfersRequest(
        token_address=token_address,
        partner_address=partner_address,
    )
    assert request.endpoint == f"/address/{token_address}/{partner_address}"