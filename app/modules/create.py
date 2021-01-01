from app import FILE_PATH, TTL_LIST
import json
import time


# Check if duplicate key exists
def dup_search(new_key):
    with open(FILE_PATH, 'r') as f:
        for line in f:
            key = line.split("|")[0]
            if key == new_key:
                return False
    return True


# Insert Key at data store file
def key_insert(key, value, ttl):
    ttl = int(time.time())+ttl
    TTL_LIST.append(ttl)
    with open(FILE_PATH, 'a') as file:
        file.write(f"{key}|{json.dumps(value)}|{ttl}")
        file.write("\n")
