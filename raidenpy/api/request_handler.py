import requests

from raidenpy.api.request import BaseRequest, BaseResponse


class Request:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = f"{endpoint}/api/{version}"

    def do(self, request: BaseRequest) -> BaseResponse:
        """Send HTTP request to URI within defined method."""
        response = requests.request(
            method=request.method,
            url=f"{self.endpoint}{request.endpoint}",
        )
        return response