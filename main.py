import requests
from app.client import api_client


def main():
    text = input()
    api_client.save(text)


if __name__ == '__main__':
    main()
