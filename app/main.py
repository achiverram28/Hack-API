from fastapi import FastAPI,Request,Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.DB_func import mlh, devfolio , open_source , cp ,  student_dev , gdg , aws , ios , microsoft
from fastapi_jwt_auth import AuthJWT
##################################
from app.authentication.config import settings
from app.authentication.routers import auth,user 
from app.authentication import oauth2
################################
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000"
    
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static",StaticFiles(directory='./app/static'),name="static")
templates = Jinja2Templates(directory="./app/templates")
# @app.get("/users/{user_id}",response_class=HTMLResponse)
# async def read_user(request:Request,user_id:str):
#     return templates.TemplateResponse("index.html",{"request":request,"id":user_id})
########
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
# ######
@app.get("/",response_class=HTMLResponse)
def welcome(request:Request):
    return templates.TemplateResponse("welcome.html",{"request":request})
@app.get("/hackathons",response_class=HTMLResponse)
def hackathons(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return templates.TemplateResponse("hackathons.html",{"request":request})
@app.get("/hackathons/mlh",response_class=HTMLResponse)
async def mlh_hac(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = mlh.fetchAll() 
    return templates.TemplateResponse("mlh.html",{"request":request,"ans":ans})
@app.get("/hackathons/mlh.json")
def mlh_hac_all(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return mlh.fetchAll()
@app.get("/hackathons/mlh/month={month}.json")
def mlh_hac_month_json(month,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return mlh.fetch_det_month(month)
@app.get("/hackathons/mlh/month={month}",response_class=HTMLResponse)
async def mlh_hac_month(month,request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = mlh.fetch_det_month(month)
    return templates.TemplateResponse("mlh.html",{"request":request,"ans":ans})
@app.get("/hackathons/mlh/type={typee}.json")
def mlh_hac_type(typee,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return mlh.fetch_det_type(typee)
@app.get("/hackathons/mlh/type={typee}",response_class=HTMLResponse)
async def mlh_hac_month(typee,request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = mlh.fetch_det_type(typee)
    return templates.TemplateResponse("mlh.html",{"request":request,"ans":ans})
@app.get("/hackathons/devfolio.json")
def devfolio_json( Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return devfolio.fetchAll()
@app.get("/hackathons/devfolio",response_class=HTMLResponse)
async def devfolio_hac(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = devfolio.fetchAll()
    return templates.TemplateResponse("devfolio.html",{"request":request,"ans":ans})
@app.get("/hackathons/devfolio/month={month}.json")
def devfolio_mon_json(month,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return devfolio.fetch_by_mon(month)
@app.get("/hackathons/devfolio/month={month}",response_class=HTMLResponse)
async def devfolio_mon(month,request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = devfolio.fetch_by_mon(month)
    return templates.TemplateResponse("devfolio.html",{"request":request,"ans":ans})
@app.get("/hackathons/open_source.json")
def open_source_json(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return open_source.fetchAll()
@app.get("/hackathons/open_source",response_class=HTMLResponse)
async def open_source_all(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = open_source.fetchAll()
    return templates.TemplateResponse("open_source.html",{"request":request,"ans":ans})
@app.get("/hackathons/open_source/month={month}.json")
def open_source_month_json(month,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return open_source.fetch_by_mon(month)
@app.get("/hackathons/open_source/month={month}",response_class=HTMLResponse)
async def open_source_month(month,request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = open_source.fetch_by_mon(month)
    return templates.TemplateResponse("open_source.html",{"request":request,"ans":ans})
@app.get("/hackathons/open_source/name={name}.json")
def open_source_event_name_json(name,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return open_source.fetch_desc(name)
@app.get("/hackathons/open_source/name={name}/desc")
def open_source_event_desc(name,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return open_source.fetch_name_desc(name)
@app.get("/hackathons/competitive_coding.json")
def comp_coding_json(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return cp.fetchAll()
@app.get("/hackathons/competitive_coding",response_class=HTMLResponse)
async def comp_coding(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = cp.fetchAll()
    return templates.TemplateResponse("cp.html",{"request":request,"ans":ans})
# @app.get("/hackathons/more_hackathons")
# def more_hackathons():
#     return event_brite.fetchAll()

@app.get("/student_dev_support.json")
def student_dev_support_json(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return student_dev.fetchAll()
@app.get("/student_dev_support",response_class=HTMLResponse)
async def student_dev_support(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = student_dev.fetchAll()
    return templates.TemplateResponse("student_dev.html",{"request":request,"ans":ans})
@app.get("/gdg_events.json")
def gdg_events_json(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return gdg.fetchAll()
@app.get("/gdg_events",response_class=HTMLResponse)
async def gdg_events(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = gdg.fetchAll()
    return templates.TemplateResponse("gdg.html",{"request":request,"ans":ans})
@app.get("/aws_events.json")
def aws_events_json(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return aws.fetchAll()
@app.get("/aws_events/name={name}/desc")
def aws_desc(name,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return aws.fetch_name_desc(name)
@app.get("/aws_events",response_class=HTMLResponse)
async def aws_events(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = aws.fetchAll()
    return templates.TemplateResponse("student_dev.html",{"request":request,"ans":ans})
@app.get("/ios_events.json")
def ios_events_json(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return ios.fetchAll()
@app.get("/ios_events",response_class=HTMLResponse)
async def ios_events(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = ios.fetchAll()
    return templates.TemplateResponse("ios.html",{"request":request,"ans":ans})
@app.get("/ios_events/name={name}/desc")
def ios_desc(name,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return ios.fetch_name_desc(name)
@app.get("/microsoft_events.json")
def microsoft_events_json(Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    return microsoft.fetchAll()
@app.get("/microsoft_events",response_class=HTMLResponse)
async def microsoft_events(request:Request,Authorize: AuthJWT = Depends(), user_id: str = Depends(oauth2.require_user)):
    ans = microsoft.fetchAll()
    return templates.TemplateResponse("microsoft.html",{"request":request,"ans":ans})
