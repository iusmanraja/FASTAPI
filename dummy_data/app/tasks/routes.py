from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import Column, Integer, String
from sqlalchemy import Boolean

from fastapi import APIRouter, Request
from fastapi import Depends, Header
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
import sqlite3 


from dummy_data.app.tasks.schemas import User, Users, UserResponse
from dummy_data.app.tasks.schemas import UserNotFoundException


router = APIRouter()

users = []

DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind= engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/todos")
def create_todo(title:str, db:Session = Depends(get_db)):
    todo = Todo(title=title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "Messege": "Todo Created",
        "Data":todo
    }


# conn = sqlite3.connect("test.db", check_same_thread=False)
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Todos(
#         id INTEGAR PRIMARY KEY,
#         Title TEXT,
#         Completed TEXT
#         )
# """)
# conn.commit()

# @router.get("/")
# def home():
#     return{
#         "Messege": "SQLite Connected Fine"
#     }

# def varify_token(token:str = Header(None)):
#     if token != "223344":
#         raise HTTPException(
#             status_code=401,
#             detail= "UnAuthorized"
#             )
#     return {"user": "Authoried User"}


# @router.get("/secure-data")
# def secure_data(user = Depends(varify_token)):
#     return{
#         "Messege":"Secure Data Accessed",
#         "user":user
#     }


# def get_current_user():
#     return{
#         "User":"Usman"
#     }

# @router.get("/profile")
# def profile(user = Depends(get_current_user)):
#     return user


# @router.get("/dashboard")
# def dashboard(user = Depends(get_current_user)):
#     return user



# @router.post("/users", status_code=status.HTTP_201_CREATED)
# def create_user(user: User):
#     users.append(user)
#     return {
#         "Status": "Success Fully",
#         "Message": "User Created",
#         "data": user
#     }

# @router.get("/user/{name}")
# def get_user(name:str):
#     if name !=  "Usman":
#         raise UserNotFoundException(name)
#     return{
#         "Name":name
#     }

# @router.get("/users/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException (status_code=404, detail="User Not Found")
#     return{
    
#         "id":1,
#         "Name":"Usman"
#     }



# @router.put("/users/{user_id}")
# def update_user(user_id: int,user: User,notify:bool = False):
#     if user_id < len(users):
#         users[user_id]= user

#         return{
#             "Messege": "User Updated",
#             "Notify":notify,
#             "Data":user
#         }
    
#     return {
#         "Error": "User Not Found"
#     }


# @router.get("/user", response_model=UserResponse)
# def get_user():
#     return{
#         "name": "Usman",
#         "age":20,
#         "password":"1234"
#     }
