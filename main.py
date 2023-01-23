from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from DB_func import mlh
app = FastAPI()
origins = [
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
@app.get("/hackathons/mlh")
def mlh_hac_all():
    return mlh.fetchAll()
@app.get("/hackathons/mlh/month={month}")
def mlh_hac_month(month):
    return mlh.fetch_det_month(month)
@app.get("/hackathons/mlh/type={typee}")
def mlh_hac_type(typee):
    return mlh.fetch_det_type(typee)
    
