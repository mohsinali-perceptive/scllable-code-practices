from ..connector_type import ConnectorType
from .utils import transorm_json_to_zoho

class ZohoConnector(ConnectorType):
    def __init__(self, payload, api_key):
        super().__init__(payload)
        self._api_key = api_key

    def transform(self):
        return transorm_json_to_zoho(self, payload=self._payload)

    def send(self, payload):
        print(f"pushing into zoho with api_key {self._api_key}")
        print("payload -> ", payload)
