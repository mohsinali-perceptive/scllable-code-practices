"""
Derived or child classes must be able to replace their base or parent classes

"""

from abc import ABC, abstractmethod


# Base class for shapes
class Rectangle(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @abstractmethod
    def area(self):
        return self._width * self._height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    @abstractmethod
    def set_width(self, width):
        self._width = width

    @abstractmethod
    def set_height(self, height):
        self._height = height


# Derived class for squares
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def set_width(self, width):
        self._width = self._height = width

    def set_height(self, height):
        self._width = self._height = height

    def area(self):
        return self._width * self._height


if __name__ == "__main__":
    s = Square(5)
    s.set_width(10)
    print(f"Area: {s.area()}")


"""
Rectangle Class: This is the base class that has properties for width and height. It has methods for calculating the area and for setting width and height.

Square Class: This class inherits from Rectangle but overrides the setWidth and setHeight methods to ensure that changing one dimension affects the other, maintaining the property that all sides are equal.

LSP Violation Example :

To see a potential violation of LSP, consider what would happen if you were to use the Square class in a context expecting a Rectangle:
If you substitute a Square where a Rectangle is expected, changing just the width or height would lead to unexpected results because it will change both dimensions.

"""
