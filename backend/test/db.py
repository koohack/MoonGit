from pymongo import MongoClient

## ---------------------------------
## Get database -> collection (database_name, collection_name)
## ---------------------------------
def connectDB(database_name, collection_name):
    conn = MongoClient("mongodb://localhost:27017") ## config에 저장하는게 좋음
    db = conn[database_name]
    db = db[collection_name]
    return db

## ---------------------------------
## Make initial user information
## ---------------------------------
def make_user_data(name, id, password, create_at = None, last_login = None, token = None):
    out = dict()
    out["name"] = name
    out["_id"] = id
    out["password"] = password
    out["create_at"] = create_at
    out["last_login"] = last_login
    out["token"] = token
    return out

## --------------------------------
## Insert data to the collection
## (If insertion false return False, else return True)
## --------------------------------
def insert_data(db, data):
    try: db.insert_one(data)
    except: return False
    return True

## --------------------------------
## Make token for logined user
## --------------------------------
import secrets
def make_token():
    return secrets.token_urlsafe(32)

## --------------------------------
## Check whether the login is good or not.
## If login is successful update the token
## (If login is vaild return True, else return False)
## --------------------------------
def check_login(db, id, entered_password):
    userInfo = db.find_one({"_id" : id})
    if userInfo == None: return False, None

    pw = userInfo["password"]
    if pw == entered_password:
        token = make_token()
        db.update_one({"_id" : id}, { "$set" : {"token" : token}})
        return True, token
    else: return False, None

