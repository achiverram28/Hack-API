import pymongo
import certifi
import urllib
client=pymongo.MongoClient("mongodb+srv://"+urllib.parse.quote_plus("ram")+":"+urllib.parse.quote_plus("123456789!@#$%^&*")+"@api-dev.gwndkto.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["fastapi"]
User = db["users"]
# dt=[{
#     "Name":"Ram",
#     "email":"ram@ram.com"
# }]
# User.insert_many(dt)
# ans = User.find({},{'_id':False})
# ans = list(ans)
# print(ans)