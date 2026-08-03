"""
This principle applies to interfaces and is similar to the Single Responsibility Principle, focusing on keeping interfaces specific and well-defined. It states that clients should not be forced to depend on methods that are irrelevant to them, avoiding unnecessary dependencies.

"""

from abc import ABC, abstractmethod


# Interface for vegetarian menu
class IVegetarianMenu(ABC):
    @abstractmethod
    def get_vegetarian_menu(self):
        pass


# Interface for non-vegetarian menu
class INonVegetarianMenu(ABC):
    @abstractmethod
    def get_non_vegetarian_menu(self):
        pass


# Interface for drinks menu
class IDrinkMenu(ABC):
    @abstractmethod
    def get_drink_menu(self):
        pass


# Class for vegetarian menu
class VegetarianMenu(IVegetarianMenu):
    def get_vegetarian_menu(self):
        return ["Vegetable Curry", "Paneer Tikka", "Salad"]


# Class for non-vegetarian menu
class NonVegetarianMenu(INonVegetarianMenu):
    def get_non_vegetarian_menu(self):
        return ["Chicken Curry", "Fish Fry", "Mutton Biryani"]


# Class for drinks menu
class DrinkMenu(IDrinkMenu):
    def get_drink_menu(self):
        return ["Water", "Soda", "Juice"]


# Function to display menu items for a vegetarian customer
def display_vegetarian_menu(menu):
    print("Vegetarian Menu:")
    for item in menu.get_vegetarian_menu():
        print(f"- {item}")


# Function to display menu items for a non-vegetarian customer
def display_non_vegetarian_menu(menu):
    print("Non-Vegetarian Menu:")
    for item in menu.get_non_vegetarian_menu():
        print(f"- {item}")


def main():
    veg_menu = VegetarianMenu()
    non_veg_menu = NonVegetarianMenu()
    drink_menu = DrinkMenu()

    display_vegetarian_menu(veg_menu)
    display_non_vegetarian_menu(non_veg_menu)


if __name__ == "__main__":
    main()
