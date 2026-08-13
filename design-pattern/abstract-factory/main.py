"""
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It acts as a "factory of factories," where a super-factory creates other factories that in turn produce specific objects.

"""

from abc import ABC, abstractmethod


# Abstract Products
class Car(ABC):
    @abstractmethod
    def assemble(self):
        pass


class CarSpecification(ABC):
    @abstractmethod
    def display(self):
        pass


# Concrete Products


class Sedan(Car):
    def assemble(self):
        print("Assembling Sedan car.")


class Hatchback(Car):
    def assemble(self):
        print("Assembling Hatchback car.")


class NorthAmericaSpecification(CarSpecification):
    def display(self):
        print(
            "North America Car Specification: Safety features compliant with local regulations."
        )


class EuropeSpecification(CarSpecification):
    def display(self):
        print(
            "Europe Car Specification: Fuel efficiency and emissions compliant with EU standards."
        )


# Abstract Factory


class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_specification(self):
        pass


# Concrete Factories


class NorthAmericaCarFactory(CarFactory):
    def create_car(self):
        return Sedan()

    def create_specification(self):
        return NorthAmericaSpecification()


class EuropeCarFactory(CarFactory):
    def create_car(self):
        return Hatchback()

    def create_specification(self):
        return EuropeSpecification()


# Client Code


def main():
    factory = NorthAmericaCarFactory()
    car = factory.create_car()
    spec = factory.create_specification()
    car.assemble()
    spec.display()

    factory = EuropeCarFactory()
    car = factory.create_car()
    spec = factory.create_specification()
    car.assemble()
    spec.display()


if __name__ == "__main__":
    main()
