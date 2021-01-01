from app import FILE_PATH, TTL_LIST, del_index
import time


def del_key(key):
    # Check if key exists
    flag = False
    with open(FILE_PATH, 'r') as f:
        for line in f:
            keys = line.split("|")[0]
            if keys == key:
                flag = True
                break
    if flag:
        pass
    else:
        return "Key not found"

    # Store each lines
    o_file = open(FILE_PATH, "r")
    lines = o_file.readlines()
    o_file.close()

    # Find line of the key
    count = 0
    with open(FILE_PATH, 'r') as f:
        for line in f:
            skey = line.split("|")[0]
            if skey == key:
                break
            count += 1

    # Delete key line from variable lines
    del lines[count]

    # Write the file after deletion
    new_file = open(FILE_PATH, "w+")
    for nline in lines:
        new_file.write(nline)
    new_file.close()
    return "Key Deleted"


def ttl_func():
    trn = int(time.time())
    if trn in TTL_LIST:
        i = TTL_LIST.index(trn)
        del_index(i)

