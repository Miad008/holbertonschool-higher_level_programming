#!/usr/bin/python3
"""Module for serializing and deserializing a custom class using pickle."""

import pickle


class CustomObject:
    """Custom class with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # optional: log or print error

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file and return it."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
