#!/usr/bin/python3
"""Defines Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square with size validation."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate area of square."""
        return self.__size ** 2
