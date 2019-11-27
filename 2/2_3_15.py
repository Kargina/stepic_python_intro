import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kvargs):
        return json.dumps(func(*args, **kvargs))
    return wrapper
