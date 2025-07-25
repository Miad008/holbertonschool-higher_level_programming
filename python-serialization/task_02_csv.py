#!/usr/bin/python3
"""Convert CSV file to JSON and save the result."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON and write to 'data.json'."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
