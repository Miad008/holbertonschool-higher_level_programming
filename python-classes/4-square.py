#!/usr/bin/python3


"""Defines a class Square with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square with optional size."""
        self.size = size  # Use setter to initialize size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):  # Check if the value is an integer
            raise TypeError("size must be an integer")
        if value < 0:  # Check if the value is non-negative
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
