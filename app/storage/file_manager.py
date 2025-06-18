import json
import os
from datetime import date


def save_to_json(new_data):
    filename = f"days/{date.today()}.json"
    new_data = json.loads(new_data)
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                existing = json.load(file)
            except:
                existing = []
    else:
        existing = []

    existing.extend(new_data)

    with open(filename, 'w') as file:
        json.dump(existing, file, indent=4, ensure_ascii=False)


def load_from_json(data):
    filename = f"days/{data}.json"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                saved_data = json.load(file)
            except:
                saved_data = 'Error'
    else:
        saved_data = 'No data'

    return saved_data