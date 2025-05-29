#!/usr/bin/python3
"""Check if obj is instance of subclass of a_class"""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class only"""
    return is instance(obj, a_class) and type(obj) is not a_class
