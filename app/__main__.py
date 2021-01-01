from .helper.jsonhandler import get_json
from .modules.create import dup_search, key_insert
from .modules.read import produce
from .modules.delete import del_key, ttl_func
import threading


def create():
    # Validate Key
    while True:
        key = input("Key: ")
        if len(key) > 32:
            print("Key Length shouldn't be greater than 32 chars!")
        else:
            break

    # Validate and Insert JSON by file/link
    if dup_search(key):
        val = input("Enter json file location/link: ")
        res, data = get_json(val)
        ttl = None
        if res:
            try:
                ttl = int(input("Enter time to live in seconds[optional]: "))
                if ttl == '':
                    ttl = None
            except ValueError:
                print("Invalid Input!!!")
            key_insert(key, data, ttl)
            print("Data Inserted!")
        elif data == "filesize":
            print("JSON File Size shouldn't exceed 16kB !")
        elif data == "invalidlink":
            print("Invalid JSON link!")
        else:
            print("Invalid JSON file!")
    else:
        print("Duplicate Key Found!")


def read():
    key = input("Key: ")
    print(produce(key))


def delete():
    key = input("Enter key to delete: ")
    print(del_key(key))


def main():
    thread = threading.Thread(target=ttl_func())
    thread.start()
    while True:
        print("1.Create\n2.Read\n3.Delete\n4.Exit")
        try:
            choice = int(input("Enter a choice:"))
            if choice == 1:
                count = int(input("How many data you wish to input? "))
                for _ in range(count):
                    create()
                    print("---------------------------------------------")
            elif choice == 2:
                read()
            elif choice == 3:
                delete()
            else:
                exit(0)
        except ValueError:
            print("Invalid Input!")


main()
