import os
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


def main():
    print(bot('150 грам риса курица жаренная в соевом соусе 100 гр'))

if __name__ == '__main__':
    main()