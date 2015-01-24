import json
from collections import deque

class entry:
    def __init__(self):
        stuff = 0

def format_response(success, obj):
    response = {"error": not success}
    if isinstance(obj, deque):
        data = "["
        for elt in obj:
            data += elt.format() + ","
        data += "]"
        response["data"] = data
    elif isinstance(obj, entry):
        response["data"] = obj.format()
    else:
        response["data"] = json.dumps(obj)
    return json.dumps(response)
