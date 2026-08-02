from abc import ABC, abstractmethod


class PaymentType(ABC):
    @abstractmethod
    def process(self, amount: float):
        pass
