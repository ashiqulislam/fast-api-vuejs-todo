from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordRequestForm
from app.controllers import auth_controller
from app.database import get_db
from app.schemas import UserCreate, LoginRequest

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return auth_controller.create_user(user, db)

@router.post("/login")
def login(form_data: LoginRequest, db: Session = Depends(get_db)):
    user = auth_controller.authenticate_user(form_data.email, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Invalid credentials")
    token = auth_controller.create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer", "user": user}
