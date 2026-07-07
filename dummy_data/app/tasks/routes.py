from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dummy_data.app.database import get_db
from dummy_data.app.models import Todo

router = APIRouter()


@router.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):

    todo = Todo(
        title=title,
        completed=False
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return {
        "Message": "Todo Created",
        "Data": todo
    }



@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):

    todos = db.query(Todo).all()

    return {
        "Total": len(todos),
        "Data": todos
    }



@router.get("/todos/{todo_id}")
def get_todo(todo_id=int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    return todo



@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, title:str, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id ==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    todo.title = title

    db.commit()
    db.refresh(todo)

    return{
        "Messege": "TODO Updated",
        "Data": todo
    }


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    
    db.delete(todo)
    db.commit()
    

    return{
        "Messege": "TODO DELETED",
        "Data": todo
    }