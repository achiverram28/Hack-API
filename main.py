from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from DB_func import mlh, devfolio , open_source , cp , event_brite, student_dev , gdg , aws , ios , microsoft

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
@app.get("/hackathons/mlh",response_class=HTMLResponse)
async def mlh_hac(request:Request):
    ans = mlh.fetchAll() 
    return templates.TemplateResponse("mlh.html",{"request":request,"ans":ans})
@app.get("/hackathons/mlh.json")
def mlh_hac_all():
    return mlh.fetchAll()
@app.get("/hackathons/mlh/month={month}.json")
def mlh_hac_month(month):
    return mlh.fetch_det_month(month)
@app.get("/hackathons/mlh/type={typee}.json")
def mlh_hac_type(typee):
    return mlh.fetch_det_type(typee)
@app.get("/hackathons/devfolio.json")
def devfolio_json():
    return devfolio.fetchAll()
@app.get("/hackathons/devfolio",response_class=HTMLResponse)
async def devfolio_hac(request:Request):
    ans = devfolio.fetchAll()
    return templates.TemplateResponse("devfolio.html",{"request":request,"ans":ans})
@app.get("/hackathons/devfolio/month={month}.json")
def devfolio_mon(month):
    return devfolio.fetch_by_mon(month)
@app.get("/hackathons/open_source.json")
def open_source_json():
    return open_source.fetchAll()
@app.get("/hackathons/open_source",response_class=HTMLResponse)
async def open_source_all(request:Request):
    ans = open_source.fetchAll()
    return templates.TemplateResponse("open_source.html",{"request":request,"ans":ans})
@app.get("/hackathons/open_source/month={month}.json")
def open_source_month(month):
    return open_source.fetch_by_mon(month)
@app.get("/hackathons/open_source/name={name}.json")
def open_source_event_name(name):
    return open_source.fetch_desc(name)
@app.get("/hackathons/open_source/name={name}/desc")
def open_source_event_desc(name):
    return open_source.fetch_name_desc(name)
@app.get("/hackathons/competitive_coding.json")
def comp_coding_json():
    return cp.fetchAll()
# @app.get("/hackathons/more_hackathons")
# def more_hackathons():
#     return event_brite.fetchAll()

@app.get("/student_dev_support.json")
def student_dev_support_json():
    return student_dev.fetchAll()
@app.get("/student_dev_support",response_class=HTMLResponse)
async def student_dev_support(request:Request):
    ans = student_dev.fetchAll()
    return templates.TemplateResponse("student_dev.html",{"request":request,"ans":ans})
@app.get("/gdg_events.json")
def gdg_events_json():
    return gdg.fetchAll()
@app.get("/gdg_events",response_class=HTMLResponse)
async def gdg_events(request:Request):
    ans = gdg.fetchAll()
    return templates.TemplateResponse("gdg.html",{"request":request,"ans":ans})
@app.get("/aws_events.json")
def aws_events_json():
    return aws.fetchAll()
@app.get("/aws_events/name={name}/desc")
def aws_desc(name):
    return aws.fetch_name_desc(name)
@app.get("/aws_events",response_class=HTMLResponse)
async def aws_events(request:Request):
    ans = aws.fetchAll()
    return templates.TemplateResponse("student_dev.html",{"request":request,"ans":ans})
@app.get("/ios_events.json")
def ios_events_json():
    return ios.fetchAll()
@app.get("/ios_events",response_class=HTMLResponse)
async def ios_events(request:Request):
    ans = ios.fetchAll()
    return templates.TemplateResponse("ios.html",{"request":request,"ans":ans})
@app.get("/ios_events/name={name}/desc")
def ios_desc(name):
    return ios.fetch_name_desc(name)
@app.get("/microsoft_events.json")
def microsoft_events_json():
    return microsoft.fetchAll()
@app.get("/microsoft_events",response_class=HTMLResponse)
async def microsoft_events(request:Request):
    ans = microsoft.fetchAll()
    return templates.TemplateResponse("microsoft.html",{"request":request,"ans":ans})
