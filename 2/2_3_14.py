import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def get_key(key):
    try:
        with open(storage_path, 'r') as fi:
            data = json.loads(json.load(fi))
        # print(type(data))
        print (', '.join(data[key]))
    except FileNotFoundError:
        pass

def write_key_val(key, val):

    if (not os.path.exists(storage_path)) or (os.stat(storage_path).st_size == 0):
    # if no file or file is empty -> write new
        with open(storage_path, 'w') as fi:
            data = json.dumps({f'{key}': [f'{val}']})
            json.dump(data, fi)
        
    else:
    # if file not empty -> add to end of dict
        with open(storage_path, 'r') as fi:
            data = json.loads(json.load(fi))
        if key in data:
        # if key exists in data
            value = list(data[key])
            value.append(val)
            data[key] = value
        else:
        #if key NOT exists in data
            rere = []
            rere.append(val)
            data[key] = rere
        with open(storage_path, 'w') as fi:
            data = json.dumps(data)
            json.dump(data, fi)

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key")
parser.add_argument("--val", help="value of key")
args = parser.parse_args()

if args.key and args.val is None:
    get_key(args.key)
elif args.key and args.val:
    write_key_val(args.key, args.val)