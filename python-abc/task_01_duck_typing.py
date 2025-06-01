#!/usr/bin/env python3
"""
Defines an abstract class 'Shape' and two subclasses 'Circle' and 'Rectangle'.
Includes 'shape_info' to print area and perimeter using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    Shapes must implement methods to calculate area and perimeter.
    """
    @abstractmethod
    def area(self):
        """Calculate and return the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter."""
        pass


class Circle(Shape):
    """
    Circle class that implements area and perimeter calculations.
    Handles negative radius using abs().
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Rectangle class for area and perimeter calculations.
    Takes width and height as inputs.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter using duck typing.
    Assumes the object has 'area' and 'perimeter' methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
