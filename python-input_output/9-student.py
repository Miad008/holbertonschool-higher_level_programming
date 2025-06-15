#!/usr/bin/python3
"""
This module defines a Student class with basic attributes and a method
to return its dictionary representation.
"""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of the Student instance."""
        return self.__dict__
