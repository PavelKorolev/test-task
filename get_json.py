import json
import sys

def get_json(json_name):
    try:
        with open(json_name) as json_file:
            input = json.load(json_file)
    except IndexError:
        print("invalid arguments")
        return None
    except FileNotFoundError:
        print("json not exist")
        return None
    except json.JSONDecodeError:
        print("invalid format")
        return None
    
    return input

