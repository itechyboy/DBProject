from app import FILE_PATH
import json


# Check if duplicate key exists
def dup_search(new_key):
    with open(FILE_PATH, 'r') as f:
        for line in f:
            key = line.split("|")[0]
            if key == new_key:
                return False
    return True


# Insert Key at data store file
def key_insert(key, value):
    with open(FILE_PATH, 'a') as file:
        file.write(f"{key}|{json.dumps(value)}")
        file.write("\n")
