from pydantic import BaseModel



class User(BaseModel):
    name:str
    age:int


class Users(BaseModel):
    name:str
    age:int
    password:str


class UserResponse(BaseModel):
    name:str
    age:int


class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name