from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from datetime import date
from app.client import api_client

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/webgui/static"), name="static")
templates = Jinja2Templates(directory='app/webgui/templates')

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    macros = api_client.load(date.today())
    total_macros = api_client.get_total_macros(date.today())
    return templates.TemplateResponse('index.html', {"request": request, "data": date.today(), 'macros': macros, 'total_macros': total_macros})


@app.post('/save_data')
async def save_data(request: Request):
    form = await request.form()
    products = form.get("products")
    api_client.save(products)
    return RedirectResponse(url='/', status_code=303)