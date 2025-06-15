#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
then saves them in a JSON file.
"""


import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data if file exists, otherwise start with empty list
if os.path.exists(filename):
    data = load_from_json_file(filename)
else:
    data = []

# Add new items from command line arguments
data.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(data, filename)
