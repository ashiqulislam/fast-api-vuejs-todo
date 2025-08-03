from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middleware import CustomResponseMiddleware
from app.database import Base, engine
from app.routes import auth_routes, todo_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(  title="Your API Title",
    version="1.0.0",  # ✅ Required
    openapi_version="3.1.0" )
# Allow CORS for frontend dev server
origins = [
    "http://localhost:5173",  # Vite (Vue/React) dev server
    "http://127.0.0.1:5173"
]
app.add_middleware(CustomResponseMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(todo_routes.router, prefix="/todos", tags=["Todos"])