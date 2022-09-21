from multiprocessing import connection
import os 
from pymongo import MongoClient

connection_string="mongodb+srv://karthik:karthik@cluster0.rctxccl.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(connection_string)

data=client.list_database_names()
print(data)
dataSeesaws=client.Seesaws
collections=dataSeesaws.list_collection_names()
print(collections)
collection=dataSeesaws.Users
user_input = {'firstName': 'karthik', 'lastName': 'katakam', 'email': 'kk@gmail.com' , 'Mobile': '7382909540' , 'Password': 'password1'}
#collection.insert_one(user_input)
datacol=collection.find()
print(datacol)
#for d in datacol:
    #print(d)
kname=collection.find_one({"firstName":"karthik"})
print(kname)
if kname :
    print("a")
#countofdocuments=collection.find().count()
#print(countofdocuments)