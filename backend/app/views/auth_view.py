from pydantic import BaseModel

class AuthResponse(BaseModel):
    message: str
    status: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
