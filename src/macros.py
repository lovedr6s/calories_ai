import os
import json
from datetime import date
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('ChatGPTApi'))
prompt = os.getenv('prompt')


def get_macros(products):
    response = client.responses.create(
        model= "gpt-4.1-nano",
        input = prompt + products
    )
    return response.output_text


def save_to_json(new_data):
    filename = f"{date.today()}.json"
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

def load_from_json():
    pass