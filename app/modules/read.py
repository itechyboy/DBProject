from app import FILE_PATH
import json


def produce(new_key):
    # Check if key exists and get value
    with open(FILE_PATH, 'r') as f:
        for line in f:
            key = line.split("|")[0]
            if key == new_key:
                val = line.split("|")[1]
                data = json.loads(val)
                return data
    return "No Results Found"
