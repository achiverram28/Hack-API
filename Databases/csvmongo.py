## This file converts csv to the mongoDB DataBase
import pandas as pd
import pymongo
import urllib
import certifi
df = pd.read_csv('Hac1.csv')
df_1=pd.read_csv("Hackathons_database.csv")
df_2=pd.read_csv("Hac2.csv")
df_3=pd.read_csv("Hac3.csv")
df_4=pd.read_csv("Hac4.csv")
df_5=pd.read_csv("Hac5.csv")
df_6=pd.read_csv("Hac6.csv")
df_7=pd.read_csv("Hac7.csv")
df_8=pd.read_csv("Hac8.csv")
df_9=pd.read_csv("Hac9.csv")
# print(df.head())
data = df.to_dict(orient="records")
data_1=df_1.to_dict(orient="records")
data_2=df_2.to_dict(orient="records")
data_3=df_3.to_dict(orient="records")
data_4=df_4.to_dict(orient="records")
data_5=df_5.to_dict(orient="records")
data_6=df_6.to_dict(orient="records")
data_7=df_7.to_dict(orient="records")
data_8=df_8.to_dict(orient="records")
data_9=df_9.to_dict(orient="records")
# print(data)
client=pymongo.MongoClient("mongodb+srv://"+urllib.parse.quote_plus("ram")+":"+urllib.parse.quote_plus("123456789!@#$%^&*")+"@api-dev.gwndkto.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
### Dont forget to add tlsCAFile=certifi.where() for ssl certification , by installing pip3 install certifi
# print(client.test)
# def checkExistence_DB(DB_NAME,client):
#     """To check whether the database is present or not """
#     DBlist=client.list_database_names()
#     if DB_NAME in DBlist:
#         print("Database {} already exists".format(DB_NAME))
#         return True
#     print("Database {} does not exist".format(DB_NAME))
#     return False
# check = checkExistence_DB("hackathons-db",client)
# print(check)
# print(client.list_database_names()) 
db=client["Hackathons"]
# print(client.list_database_names()) 
# print(db.list_collection_names())
COLLECTION_NAME="EventBriteHackathons"
collection=db[COLLECTION_NAME]
# print(db.list_collection_names())
collection.insert_many(data)
COLLECTION_NAME_1="MLH-Hackathons"
collection_1=db[COLLECTION_NAME_1]
collection_1.insert_many(data_1)
COLLECTION_NAME_2="Devfolio-Hackathons"
collection_2=db[COLLECTION_NAME_2]
collection_2.insert_many(data_2)
COLLECTION_NAME_3 = "GDG-Events"
collection_3=db[COLLECTION_NAME_3]
collection_3.insert_many(data_3)
COLLECTION_NAME_4="Open-Source-Hackathons"
collection_4=db[COLLECTION_NAME_4]
collection_4.insert_many(data_4)
COLLECTION_NAME_5="Student-Developer-Support"
collection_5=db[COLLECTION_NAME_5]
collection_5.insert_many(data_5)
COLLECTION_NAME_6="Amazon-Events"
collection_6=db[COLLECTION_NAME_6]
collection_6.insert_many(data_6)
COLLECTION_NAME_7="Microsoft-Events"
collection_7=db[COLLECTION_NAME_7]
collection_7.insert_many(data_7)
COLLECTION_NAME_8="iOS-Events"
collection_8=db[COLLECTION_NAME_8]
collection_8.insert_many(data_8)
COLLECTION_NAME_9="Competitive-Coding"
collection_9=db[COLLECTION_NAME_9]
collection_9.insert_many(data_9)

