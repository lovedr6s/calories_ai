import requests
from src import file

url = "http://127.0.0.1:8000/get_data"


def get_data(text):
    return requests.post(url, json={'text': text}).text


def main():
    text = input()
    file.save_to_json(get_data(text))


if __name__ == '__main__':
    main()
