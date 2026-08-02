from payment_types.credit_card import CreditCard
from payment_types.stripe import Stripe
from services.payment_processor import PaymentProcessor

credit_card = CreditCard(card_no="card-no", cvv=121)
stripe = Stripe(api_key="your-api-key")

credit_card_processor = PaymentProcessor(credit_card)
stripe_processor = PaymentProcessor(stripe)

credit_card_processor.process_payment(90)