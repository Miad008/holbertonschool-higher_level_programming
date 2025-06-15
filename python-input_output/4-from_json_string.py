#!/usr/bin/python3
"""
This module provides a function that returns a Python object
from a JSON string.
"""


import json


def from_json_string(my_str):
    """Convert a JSON string to a Python object."""
    return json.loads(my_str)
