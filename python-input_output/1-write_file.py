#!/usr/bin/python3
"""
This module provides a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write text to a UTF8 file and return number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
