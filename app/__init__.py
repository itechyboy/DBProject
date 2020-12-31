from .helper.filehandler import FileHandler
from os import path, remove
import pickle


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
        pass
    else:
        print("Previous file is missing! Removing saved location info!")
        remove("path.pickle")
        get_loc()
else:
    get_loc()


JSON_FILE_LIMIT = 16384
