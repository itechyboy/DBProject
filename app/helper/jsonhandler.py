import os
import requests
import json
from app import JSON_FILE_LIMIT


def get_json(file):
    if os.path.isfile(file):
        fl = open(file, 'r')
        try:
            if len(fl.read()) <= JSON_FILE_LIMIT:
                fl.close()
                pass
            else:
                fl.close()
                return False, "filesize"
            with open(file, 'r') as f:
                data = json.load(f)
            return True, data
        except json.decoder.JSONDecodeError:
            return False, "invalidfile"
    elif requests.get(file).text:
        try:
            data = requests.get(file).text
            if len(data) <= JSON_FILE_LIMIT:
                data = json.loads(data)
                return True, data
            else:
                return False, "filesize"
        except json.decoder.JSONDecodeError:
            return False, "invalidlink"
    else:
        return False, None
