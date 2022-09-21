from pymongo import MongoClient
from dotenv import load_dotenv , find_dotenv
import os 

load_dotenv(find_dotenv())
password=os.environ.get("MONGODB_PWD")
connection_string=f"mongodb+srv://karthik:{password}@cluster0.rctxccl.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(connection_string)
dataSeesaws=client.Seesaws
collection=dataSeesaws.Users