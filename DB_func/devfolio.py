import pymongo
import urllib
import certifi
client=pymongo.MongoClient("mongodb+srv://"+urllib.parse.quote_plus("ram")+":"+urllib.parse.quote_plus("123456789!@#$%^&*")+"@api-dev.gwndkto.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["Hackathons"]
events = db["Devfolio_Hackathons"]
def fetchAll():
    x = events.find({},{'_id':False,"Unnamed: 0":False})
    li=[]
    for ob in x:
        li.append(ob)
    return li
def fetch_by_mon(month):
    x = events.find({"Month":month},{'_id':False,"Unnamed: 0":False})
    li=[]
    for ob in x:
        li.append(ob)
    return li
