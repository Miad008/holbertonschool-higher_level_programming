#!/usr/bin/python3
"""Rectangle class with validated private width and height."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with width and height validated as positive integers."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height (private)."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return string representation of Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
