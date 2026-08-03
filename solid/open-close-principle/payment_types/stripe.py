from .payment_type import PaymentType

class Stripe(PaymentType):
    def __init__(self, api_key: str):
        self.__api_key = api_key
    
    def process(self, amount):
        print("stripe payment process -> ", amount)