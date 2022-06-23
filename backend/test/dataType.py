from pydantic import BaseModel

class loginData(BaseModel):
    userID : str
    userPW : str
