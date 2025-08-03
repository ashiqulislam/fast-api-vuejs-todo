from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.controllers import todo_controller
from app.database import get_db
from app.schemas import TodoCreate, TodoUpdate
import os



router = APIRouter()
SECRET_KEY = os.getenv("SECRET_KEY", "secret123")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Properly inject token via Depends here
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
        return user_id
    except (JWTError, ValueError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@router.get("/")
def list_todos(user_id: int = Depends(get_current_user),db: Session = Depends(get_db)):
    return todo_controller.get_todos(db, user_id)

@router.post("/")
def create_todo(todo: TodoCreate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    # user_id = get_current_user(token, db)
    return todo_controller.create_todo(todo, db, user_id)

@router.put("/{id}")
def update_todo(id: int, todo: TodoUpdate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    # user_id = get_current_user(token, db)
    return todo_controller.update_todo(id, todo, db, user_id)

@router.delete("/{id}")
def delete_todo(id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    # user_id = get_current_user(token, db)
    return todo_controller.delete_todo(id,  db, user_id)
