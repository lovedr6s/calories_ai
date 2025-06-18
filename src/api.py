import json
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from .macros import get_macros

app = FastAPI()


class BigText(BaseModel):
    text: str


@app.post('/get_data', response_class=PlainTextResponse)
def get_data(payload: BigText):
  text = payload.text
  while True:
    try:
        macros_data = get_macros(text)
        json.loads(macros_data)
        break
    except json.decoder.JSONDecodeError:
        print("Trying again..")
  return macros_data



'''
curl -X POST http://127.0.0.1:8000/get_data \
  -H "Content-Type: application/json" \
  -d '{"text": "hi"}'
'''