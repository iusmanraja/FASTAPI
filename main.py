from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "Messege":"TODO Added","data":todo
    }

@app.get("/todos")
def get_todos():
    return todos


@app.get("/todos{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return{"Error":"TODO Not Found"} 


@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "Messesge":"DATA UPDATED",
                "data": updated_todo
            }
        
    return{"Error":"TODO Not Found"} 

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"Messege":"Data Deleted"}

    return{"Error":"TODO Not Found"} 



# class Address(BaseModel):
#     city:str
#     pincode:str

# class User(BaseModel):
#     name:str
#     age:int
#     address:Address

# @app.post("/create_user")
# def create_user(user:User):
#     return user