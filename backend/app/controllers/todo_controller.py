from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import HTTPException
from app import models, schemas

def get_todos(db: Session, user_id: int):
    return db.query(models.Todo).filter(models.Todo.owner_id == user_id).order_by(desc(models.Todo.id)).all()

def create_todo(todo: schemas.TodoCreate, db: Session, user_id: int):
    db_todo = models.Todo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session, user_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == user_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.title = todo.title
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(todo_id: int, db: Session, user_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == user_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return db_todo
