from pydantic import BaseModel

class loginData(BaseModel):
    id : str
    pw : str
