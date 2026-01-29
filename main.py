from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# --------- Модель User ---------
class User(BaseModel):
    id: int
    username: str
    email: str

# --------- Модель для створення користувача ---------
class UserCreate(BaseModel):
    username: str
    email: str

# --------- Тимчасовий список користувачів ---------
users: List[User] = [
    User(id=1, username="admin", email="admin@example.com"),
    User(id=2, username="user1", email="user1@example.com"),
]

# --------- 1. Отримати всіх користувачів ---------
@app.get("/users", response_model=List[User])
def get_users():
    return users

# --------- 2. Отримати користувача за ID ---------
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Користувача не знайдено")

# --------- 3. Створити нового користувача ---------
@app.post("/create_user", response_model=User)
def create_user(user: UserCreate):
    new_id = users[-1].id + 1 if users else 1

    new_user = User(
        id=new_id,
        username=user.username,
        email=user.email
    )

    users.append(new_user)
    return new_user
