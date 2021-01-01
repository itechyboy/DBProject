from .helper.filehandler import FileHandler
from os import path, remove
import pickle
import time

TTL_LIST = []
JSON_FILE_LIMIT = 16384


def del_index(index):
    del TTL_LIST[index]

    o_file = open(FILE_PATH, "r")
    lines = o_file.readlines()
    o_file.close()

    del lines[index]

    new_file = open(FILE_PATH, "w+")
    for nline in lines:
        new_file.write(nline)
    new_file.close()


def load_ttl():
    with open(FILE_PATH, 'r') as f:
        for line in f:
            key = int(line.split("|")[2].replace("\n", ""))
            TTL_LIST.append(key)


def del_invalid():
    trnow = int(time.time())
    for ti in range(len(TTL_LIST)):
        if TTL_LIST[ti] <= trnow:
            del_index(ti)
            del_invalid()
            break
        else:
            break


# Get location for database and store it
def get_loc():
    global FILE_PATH
    fh = FileHandler(input("Enter location to save file [remove slash at end]: "))
    FILE_PATH = f"{fh.fpath}{fh.fname}"
    with open('path.pickle', 'wb') as fpp:
        pickle.dump(FILE_PATH, fpp)


# Check if info on location exists
if path.exists("path.pickle"):
    with open("path.pickle", "rb") as fp:
        FILE_PATH = pickle.load(fp)
    if path.exists(FILE_PATH):
        load_ttl()
        del_invalid()
        pass
    else:
        print("Previous file is missing! Removing saved location info!")
        TTL_LIST = []
        remove("path.pickle")
        get_loc()
else:
    get_loc()

