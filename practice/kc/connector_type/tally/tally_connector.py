from ..connector_type import ConnectorType
from .utils import transform_to_xml

class TallyConnector(ConnectorType):
    def __init__(self, payload, port, host):
        super().__init__(payload=payload)
        self._port = port
        self._host = host

    def transform(self, payload):
        return transform_to_xml(payload)

    def send(self, payload):
        print(f"pusing to tally on {self._port}")
        print("payload -> ", payload)

