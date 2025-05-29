#!/usr/bin/python3
"""Defines Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with validated width and height."""

    def __init__(self, width, height):
        """Initialize rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
