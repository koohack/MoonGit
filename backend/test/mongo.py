from pymongo import MongoClient
from db import *
import pandas as pd
import pymongo

conn = MongoClient("mongodb://localhost:27017")
db = conn["user"]
db = db["userInfo"]

user1 = make_user_data("park", "leader", "qwer1234")

db.update_one()

#a = db.find_one({"_id" : "leader"})
#print(a["password"])
#print(a["_id"])


#try:
 #   db.insert_one(user1)
#except: print("caonima")
