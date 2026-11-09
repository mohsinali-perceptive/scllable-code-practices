"""
user -> restraunt -> menu -> cart -> order -> payment -> notofication

"""

from typing import List
from abc import ABC, abstractmethod

class FoodItem:
    def __init__(self, name: str, price: float):
        self.name=name
        self.price=price

class Menu:
    def __init__(self, items: FoodItem):
        self.food_items = items

    def show_menu(self):
        print("================ Menu =================")
        for item in self.food_items:
            print(f"{item.name} ----- {item.price}")

        print("***************************************")

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.cart = []

    def get_cart(self):
        return self.cart
    def add_to_cart(self, item: FoodItem):
        self.cart.append(item)

class Restraunt:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.menus = []

    def add_menu(self, menu: Menu):
        self.menus.append(menu)

    def show_menu(self):
        for menu in self.menus:
            menu.show_menu()


class RestrauntManager:
    restraunts=[]
    def add_restrant(self, restrant: Restraunt):
        self.restraunts.append(restrant)

    def get_by_location(self, address: str):
        ans = []
        for restrant in self.restraunts:
            if(restrant.address == address):
                ans.append(restrant)
        return ans


class Order:
    def __init__(self, user: User):
        self.user = user
        self.food_items = user.get_cart()

    def print_bill(self):
        total_amount = 0
        print("-----------------------Bill--------------------")
        for item in self.food_items:
            total_amount += item.price
            print(item.name+ "    ", item.price)

        print("Total Amount is -> ", total_amount)

    def checkout(self, payment_method: str):
        amount = 0
        for item in self.food_items:
            amount += item.price
        method = PaymentFactory().get_payment_stratergy(type=payment_method)
        method.pay(amount)

class PaymentStratergy(ABC):
    @abstractmethod
    def pay(amount: float):
        pass

class UPIPaymentStratergy(PaymentStratergy):
    def pay(self, amount: float):
        print("making a upi payment of -> ", amount)

class CardPaymentStratergy(PaymentStratergy):
    def pay(self, amount: float):
        print("making a payment using card -> ", amount)

class PaymentFactory:
    def get_payment_stratergy(self, type: str):
        if(type == "upi"):
            return UPIPaymentStratergy()
        return CardPaymentStratergy()



##################################################

user = User("dev", "dev@gmail.com")

f1 = FoodItem("paneer", 200)
f2 = FoodItem("sharwma", 100)
f3= FoodItem("chinees roll", 300)
f4 = FoodItem("manchav noodless", 50)
f5 = FoodItem("rice", 400)
f6 = FoodItem("dosa", 200)
f7 = FoodItem("mix potato", 150)
f8 = FoodItem("cheez naan", 50)

m1 = Menu([f1,f2,f3])
m2 = Menu([f3, f4, f5])
m3 = Menu([f6, f7, f8])

r1=Restraunt("magic masala", "add1")
r2=Restraunt("magic much", "add2")
r3=Restraunt("fire on wheels", "add3")

r1.add_menu(m1)
r2.add_menu(m2)
r3.add_menu(m3)

rm = RestrauntManager()
rm.add_restrant(r1)
rm.add_restrant(r2)
rm.add_restrant(r3)

user.add_to_cart(f2)
user.add_to_cart(f4)
user.add_to_cart(f7)

order = Order(user)

order.checkout("upi")