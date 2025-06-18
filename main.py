import requests
from app.client import api_client


def main():
    text = input()
    #api_client.save(text)
    print(api_client.load('2025-06-18'))


if __name__ == '__main__':
    main()
