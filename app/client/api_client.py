import requests
from app.storage import file_manager


url = "http://127.0.0.1:8000/get_data"


def get_data(text):
    return requests.post(url, json={'text': text}).text


def save(text):
    file_manager.save_to_json(get_data(text))
