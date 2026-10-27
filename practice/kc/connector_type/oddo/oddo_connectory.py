from ..connector_type import ConnectorType

class OddoConnector(ConnectorType):
    def __init__(self, payload, api_key: str, token: int):
        super().__init__(payload=payload)
        self._api_key = api_key
        self._token = token

    def transform(self):
        return {
            "oddo_payload": self._payload
        }

    def send(self, payload):
        print("sending to oddu with payload -> ", payload)