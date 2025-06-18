import json
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from ..services.macros import get_macros

app = FastAPI()


class BigText(BaseModel):
    text: str


@app.post('/get_data', response_class=PlainTextResponse)
def get_data(payload: BigText):
  text = payload.text
  for repeat in range(5):
    try:
        if repeat == 5:
           return 'Error. Try to write other sentence'
        macros_data = get_macros(text)
        json.loads(macros_data)
        break
    except json.decoder.JSONDecodeError:
        print("Trying again..")
  return macros_data
