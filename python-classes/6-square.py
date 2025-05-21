#!/usr/bin/python3

"""Defines a class Square with size and position."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): A tuple of 2 positive integers for position. Default is (0, 0).
        """
        self.size = size
        self.position = position

    def __str__(self):
        """Returns a string representation of the square."""
        return "Square"

    @property
    def size(self):
        """Getter for the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for row in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
