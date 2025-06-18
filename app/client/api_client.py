import json
import requests
from app.storage import file_manager


url = "http://127.0.0.1:8000/get_data"


def get_data(text):
    return requests.post(url, json={'text': text}).text


def save(text: str) -> None:
    try:
        file_manager.save_to_json(get_data(text))
    except json.decoder.JSONDecodeError:
        print('error')


def load(data: str) -> json:
    return file_manager.load_from_json(data)


def get_total_macros(data: str):
    raw_data = file_manager.load_from_json(data)
    output = {
        'kcal': 0,
        'carbs': 0,
        'proteins': 0,
        'fats': 0   
    }
    try:
        for macro in raw_data:
            output['kcal'] += int(macro['kcal'])
            output['carbs'] += int(macro['carbs'])
            output['proteins'] += int(macro['proteins'])
            output['fats'] += int(macro['fats'])
    except TypeError:
        print('file empty')
    return output
