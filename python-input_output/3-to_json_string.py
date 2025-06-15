#!/usr/bin/python3
"""
This module provides a function that returns the JSON representation
of a Python object as a string.
"""

import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON string."""
    return json.dumps(my_obj)
