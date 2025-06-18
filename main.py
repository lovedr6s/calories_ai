import requests
from src import macros

url = "http://127.0.0.1:8000/get_data"
payloads = {'text': ""}


def main():
    text = input()
    response = requests.post(url, json={'text': text})
    print(response.text)
    #print(get_macros('150 грам риса курица жаренная в соевом соусе 100 гр'))

if __name__ == '__main__':
    main()