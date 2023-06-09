from fastapi import FastAPI, Request
from langdetect import detect
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})


@app.post("/detect")
async def detect_language(request: Request):
    form_data = await request.form()
    text = form_data["text"]
    language = detect(text)
    return templates.TemplateResponse("index.html", {"request": request, "result": language})
