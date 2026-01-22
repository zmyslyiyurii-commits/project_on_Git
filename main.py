from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Схема User (Pydantic модель для валідації даних)
class User(BaseModel):
    id: int
    username: str
    email: str

# Список користувачів (імітація бази даних)
users = [
    User(id=1, username="ivan_petrov", email="ivan@example.com"),
    User(id=2, username="olena_u", email="olena@example.com"),
    User(id=3, username="admin_tester", email="admin@test.com"),
]

# Ендпоінт для отримання всіх користувачів
@app.get("/users", response_model=List[User])
async def get_users():
    return users

# Ендпоінт для отримання одного користувача за ID
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    
    # Використовуємо HTTPException для коректної відповіді 404
    raise HTTPException(status_code=404, detail="User not found")