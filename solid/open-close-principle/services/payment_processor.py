from payment_types.payment_type import PaymentType


class PaymentProcessor:
    def __init__(self, method: PaymentType):
        self.method = method

    def process_payment(self, amount: float):
        print("!! processing payment in payment processor ")
        self.method.process(amount)
