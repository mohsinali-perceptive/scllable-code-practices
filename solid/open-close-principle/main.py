"""
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification" which means you should be able to extend a class behavior, without modifying it.

"""

from payment_types import CreditCard, Stripe
from services import PaymentProcessor

credit_card = CreditCard(card_no="card-no", cvv=121)
stripe = Stripe(api_key="your-api-key")

credit_card_processor = PaymentProcessor(credit_card)
stripe_processor = PaymentProcessor(stripe)

credit_card_processor.process_payment(210)
stripe_processor.process_payment(89)
