from abc import ABC, abstractmethod
from enum import Enum


class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class VehicleFactory:
    def get_vehicle(self, type: VehicleType) -> Vehicle:
        if type == VehicleType.CAR:
            return Car()
        elif type == VehicleType.BIKE:
            return Bike()
        else:
            raise ValueError("Invalid vehicle type")


car = VehicleFactory().get_vehicle(VehicleType.CAR)
car.start()

bike = VehicleFactory().get_vehicle(VehicleType.BIKE)
bike.start()

bike.stop()
car.stop()
