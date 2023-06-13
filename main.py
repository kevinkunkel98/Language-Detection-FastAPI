from fastapi import FastAPI, Request
from langdetect import detect
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

flag_list = ['af', 'ar', 'bg', 'bn', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'fa', 'fi', 'fr', 'gu', 'he',
'hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv', 'mk', 'ml', 'mr', 'ne', 'nl', 'no', 'pa', 'pl',
'pt', 'ro', 'ru', 'sk', 'sl', 'so', 'sq', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'zh-cn', 'zh-tw']

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": "", "text": ""})


@app.post("/detect")
async def detect_language(request: Request):
    form_data = await request.form()
    text = form_data["text"]
    language = detect(text)
    return templates.TemplateResponse("index.html", {"request": request, "result": language, "text": text})
