from .payment_type import PaymentType


class CreditCard(PaymentType):
    def __init__(self, card_no: str, cvv: int):
        self.__card_no = card_no
        self.__cvv = cvv

    def process(self, amount: float):
        print("credit card payment process -> ", amount)
