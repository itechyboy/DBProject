from os import path, getcwd, makedirs
from sys import platform


class FileHandler:
    def __init__(self, fpath=getcwd()):
        if fpath == '':
            self.fpath = getcwd()
        else:
            self.fpath = fpath
            self.checkpath()
        self.fname = "data.db"
        self.create_file()

    # Verify location and create file
    def create_file(self):
        self.verify_path()
        try:
            with open(f"{self.fpath}{self.fname}", "a+"):
                pass
        except PermissionError:
            if platform == "win32":
                self.fpath = f"{getcwd()}\\database\\"
            else:
                self.fpath = f"{getcwd()}/database/"
            print(f"Can't create directory! Default location is selected: {self.fpath}")
            try:
                makedirs(self.fpath)
            except OSError:
                pass
            with open(f"{self.fpath}{self.fname}", "a+"):
                pass
        print(f"Database Created at {self.fpath}!")

    # Try creating given location path
    def checkpath(self):
        if path.exists(self.fpath):
            return
        else:
            try:
                makedirs(self.fpath)
            except OSError:
                self.fpath = getcwd()
                print(f"Can't create directory! Database created at default location: {self.fpath}")

    # Creating default folder
    def verify_path(self):
        if self.fpath == getcwd():
            if platform == "win32":
                self.fpath = f"{self.fpath}\\database\\"
            else:
                self.fpath = f"{self.fpath}/database/"
            try:
                makedirs(self.fpath)
            except OSError:
                pass
        else:
            if platform == "win32":
                self.fpath = f"{self.fpath}\\"
            else:
                self.fpath = f"{self.fpath}/"
