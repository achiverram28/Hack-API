from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from DB_func import mlh, devfolio , open_source

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
@app.get("/hackathons/devfolio")
def devfolio_all():
    return devfolio.fetchAll()
@app.get("/hackathons/devfolio/month={month}")
def devfolio_mon(month):
    return devfolio.fetch_by_mon(month)
@app.get("/hackathons/open_source")
def open_source_all():
    return open_source.fetchAll()
@app.get("/hackathons/open_source/month={month}")
def open_source_month(month):
    return open_source.fetch_by_mon(month)
@app.get("/hackathons/open_source/name={name}")
def open_source_event_name(name):
    return open_source.fetch_desc(name)
@app.get("/hackathons/open_source/name={name}/desc")
def open_source_event_desc(name):
    return open_source.fetch_name_desc(name)
