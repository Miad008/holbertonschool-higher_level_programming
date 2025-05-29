#!/usr/bin/python3
"""Defines BaseGeometry class with area method"""


class BaseGeometry:
    """BaseGeometry with unimplemented area method"""
    def area(self):
        """Raises exception for unimplemented area"""
        raise Exception("area() is not implemented")
