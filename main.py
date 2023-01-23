from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()
app.mount("/static",StaticFiles(directory='static'),name="static")
templates = Jinja2Templates(directory="templates")
# @app.get("/users/{user_id}",response_class=HTMLResponse)
# async def read_user(request:Request,user_id:str):
#     return templates.TemplateResponse("index.html",{"request":request,"id":user_id})
@app.get("/",response_class=HTMLResponse)
def welcome(request:Request):
    return templates.TemplateResponse("welcome.html",{"request":request})
@app.get("/hackathons",response_class=HTMLResponse)
def hackathons(request:Request):
    return templates.TemplateResponse("hackathons.html",{"request":request})
    