# FastAPI Todo API 📝

A simple, token-based authenticated Todo API built with FastAPI, SQLAlchemy, JWT, and Docker.

---

## ✨ Features

- ✅ User authentication with JWT (access token)
- ✅ OAuth2 password flow with bearer tokens
- ✅ CRUD operations for Todos (Create, Read, Update, Delete)
- ✅ Swagger UI docs (`/docs`)
- ✅ Dockerized development environment
- ✅ Secure route access via token

---

## 📦 Tech Stack

- FastAPI
- PostgreSQL / MariaDB
- SQLAlchemy
- Pydantic
- JWT (via `python-jose`)
- Docker + Docker Compose
- Vue 3 frontend

---

## 🛠 Project Structure
```
app/
├── controllers/ # Business logic
├── database.py # DB connection
├── models.py # SQLAlchemy models
├── routes/ # FastAPI routers
│ └── todo_routes.py
├── schemas.py # Pydantic schemas
├── main.py # App entrypoint
└── auth.py # JWT creation & verification
```



---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/fastapi-todo-api.git
cd fastapi-todo-api
```

### Create .env
```
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@db:5432/db_name
```

Or for MariaDB:
```
DATABASE_URL=mysql+pymysql://user:password@db:3306/db_name
```

### 3. Start with Docker
```
docker-compose up --build
```

The API will be running at:
```
http://localhost:8000
```

### 4. Docs & Testing
Open:
```
📘 Swagger UI → http://localhost:8000/docs
🔍 ReDoc → http://localhost:8000/redoc
```


🔐 Authentication
Login using /auth/login with email and password.

Copy the returned access_token.

Click "Authorize" in Swagger docs and paste:
Bearer <your-token>


🧪 Todo Endpoints
| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/todos/`     | List all todos    |
| POST   | `/todos/`     | Create a new todo |
| PUT    | `/todos/{id}` | Update a todo     |
| DELETE | `/todos/{id}` | Delete a todo     |
All endpoints require a valid JWT token.

📄 License
MIT © [Ashiqul Islam](https://github.com/ashiqulislam) 
