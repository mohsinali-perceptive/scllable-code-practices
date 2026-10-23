from abc import ABC, abstractmethod

class ConnectorType(ABC):
    def __init__(self, payload):
        self._payload = payload

    @abstractmethod
    def transform(self, payload):
        pass

    def push(self):
        print("pusing document to accounting software... ")
        transformed_payload = self.transform(self._payload)
        self.send(transformed_payload)

    @abstractmethod
    def send(self, payload):
        pass
