from fastapi import FastAPI, Request, Form
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from loguru import logger
from typing import List
from db import *
import datetime
import aiofiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")

## ---------------------------
## Initial Login Page
## ---------------------------
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request" : request, "json_data" : {"test" : "ok"}})

## ---------------------------
## Check user id and password
## ---------------------------
@app.post("/login/")
async def checkLogin(request : Request):#info: loginData):
    ## User ID and Password
    data = await request.json()
    userID = data["userID"]
    userPW = data["userPW"]

    ## Start Login
    logger.debug("{0} | {1}(user) is trying to login."
                 .format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), userID))

    ## Connect the DB
    db = connectDB("user", "userInfo")
    flag, token = check_login(db, userID, userPW)

    ## Dummy
    context = {}
    context["request"] = request

    ## Login success
    if flag:
        ## Logging
        logger.debug("{0} | {1}(user) login successful!"
                    .format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), userID))
        ## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        ## This is test template, Please change this one
        ## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        header = {"check" : "True"}
        response = templates.TemplateResponse("MainPage.html", context, headers=header)
        expire_time = datetime.datetime.now() + datetime.timedelta(hours=1)

        ## Set cookies
        response.set_cookie(key="userID", value=userID,
                            secure=True, httponly=True, samesite='none',
                            expires=expire_time.strftime("%Y-%m-%d %H:%M:%S"))
        response.set_cookie(key="access_token_moongit", value=token,
                            secure=True, httponly=True, samesite='none',
                            expires=expire_time.strftime("%Y-%m-%d %H:%M:%S")
                            )
        return response
    ## Login False
    else:
        ## Logging
        logger.warning("{0} | {1}(user) login false!"
                    .format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), userID))

        ## Set Response
        header = {"check" : "False"}
        dummy = {}
        response = JSONResponse(content=jsonable_encoder(dummy), headers=header)

        ## Set cookies
        return response

## ---------------------------
## Get files from html
## ---------------------------
@app.post("/upload/")
async def fileUpdate(request : Request):
    #temp = request.cookies
    data = await request.form()
    data = data.get("file0")

    ## file name
    filename = data.filename
    file = data.file

    async with aiofiles.open(filename, 'wb') as outFile:
        content = file.read()
        await outFile.write(content)

    ## Get files
    #logger.debug("{0}".format(data.file))
    return {"test" : "ok"}

## ---------------------------
## Send files to html
## ---------------------------
@app.post("/sendfile/")
async def fileSender(request : Request):
    fileName = "1.testfile.pdf"
    return FileResponse(fileName)