import requests


def save(text: str) -> None:
    url = 'https://macrosapi-production.up.railway.app/save_data'
    payload = {
        'text': text,
        "user_token": "1"
    }
    requests.post(url, json=payload)


def load(data: str):
    url = "https://macrosapi-production.up.railway.app/get_data"
    headers = {
        "user-token": "1"
    }
    params = {
        "date": data
    }

    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    return response.json()



def get_total_macros(data: str):
    raw_data = load(data)
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
