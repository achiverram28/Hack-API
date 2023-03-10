import pymongo
import urllib
import certifi
client=pymongo.MongoClient("mongodb+srv://"+urllib.parse.quote_plus("ram")+":"+urllib.parse.quote_plus("123456789!@#$%^&*")+"@api-dev.gwndkto.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["Hackathons"]
events = db["Amazon-Events"]
def fetchAll():
    x = events.find({},{'_id':False,"Unnamed: 0":False})
    li=[]
    for ob in x:
        if ob in li:
            continue
        li.append(ob)
    return li
def fetch_desc(name):
    s = name.split("_")
    st=""
    for it in s:
        st=st+it+" "
    st=st.strip()
    x = events.find({"Name":st},{"_id":False,"Unnamed: 0":False})
    li=[]
    for i in x:
        if i["Name"]==st:
            if i["Name"] in li:
                continue
            li.append(i)
    return li[0]
def fetch_name_desc(name):
    res=fetch_desc(name)
    return [res["Description"]]