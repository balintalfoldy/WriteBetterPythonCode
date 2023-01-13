import string
import random


class Order:

    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.status = "open"

    def set_status(self, status):
        self.status = status


class Authorizer_SMS:

    def __init__(self):
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))

    def authorize(self):
        code = input("Enter SMS code: ")
        self.authorized = code == self.code

    def is_authorized(self) -> bool:
        return self.authorized

#! The payment processor has too many responsibilities
#! creating authorizer, generating sms code, actually aothorize it and then dealing with the payment itself.


class PaymentProcessor:

    def pay(self, order):
        #! move authorizer creatioin from here (pass it as a parameter or pass it in the initializer of the class)
        #! Also for dependency inversion, we should create and abstract Authorizer, and pass that type into payment processor -> separation layer, more extendable
        authorizer = Authorizer_SMS()
        #! remove the responsibility to generate sms code
        authorizer.generate_sms_code()
        authorizer.authorize()
        if not authorizer.is_authorized():
            raise Exception("Not authorized")
        print(f"Processing payment for order with id {order.id}")
        order.set_status("paid")
