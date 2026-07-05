from fastapi import APIRouter, Request, FastAPI
from fastapi import Depends, Header
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from dummy_data.app.tasks.schemas import User, Users, UserResponse
from dummy_data.app.tasks.schemas import UserNotFoundException


router = APIRouter()

app = FastAPI

users = []

def varify_token(token:str = Header(None)):
    if token != "223344":
        raise HTTPException(
            status_code=401,
            detail= "UnAuthorized"
            )
    return {"user": "Authoried User"}


@router.get("/secure-data")
def secure_data(user = Depends(varify_token)):
    return{
        "Messege":"Secure Data Accessed",
        "user":user
    }


def get_current_user():
    return{
        "User":"Usman"
    }

@router.get("/profile")
def profile(user = Depends(get_current_user)):
    return user


@router.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return user



@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return {
        "Status": "Success Fully",
        "Message": "User Created",
        "data": user
    }

@router.get("/user/{name}")
def get_user(name:str):
    if name !=  "Usman":
        raise UserNotFoundException(name)
    return{
        "Name":name
    }

@router.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException (status_code=404, detail="User Not Found")
    return{
    
        "id":1,
        "Name":"Usman"
    }



@router.put("/users/{user_id}")
def update_user(user_id: int,user: User,notify:bool = False):
    if user_id < len(users):
        users[user_id]= user

        return{
            "Messege": "User Updated",
            "Notify":notify,
            "Data":user
        }
    
    return {
        "Error": "User Not Found"
    }


@router.get("/user", response_model=UserResponse)
def get_user():
    return{
        "name": "Usman",
        "age":20,
        "password":"1234"
    }
