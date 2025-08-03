from fastapi import Depends, HTTPException
from sqlalchemy.exc import IntegrityError
import logging 
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from jose import jwt
import os
from datetime import datetime, timedelta
from app import models, schemas
from app.database import get_db

SECRET_KEY = os.getenv("SECRET_KEY", "secret123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_user(user: schemas.UserCreate, db: Session):
    try:
        hashed_password = bcrypt.hash(user.password)
        db_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        if "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )
        raise HTTPException(
            status_code=400,
            detail="Database integrity error"
        )
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)  # Show the actual error message
        )

def authenticate_user(email: str, password: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not bcrypt.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(user_id: int):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode({"sub": str(user_id), "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)
