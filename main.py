from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    cpf: str
    phone: str

users_db: List[User] = []

@app.post("/register/", response_model=User)
async def create_user(user: User) -> User:
    for user_exists in users_db:
        if user_exists.id == user.id:
            raise HTTPException(status_code=400, detail='User with this ID already exists')
    users_db.append(user)
    return user

@app.get("/users/", response_model=List[User])
async def read_users() -> List[User]:
    return users_db

@app.put("/updateuser/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User) -> User:
    for user in users_db:
        if user_id == user.id:
            user = updated_user
            return updated_user
    raise HTTPException(status_code=400, detail="User not found")


@app.delete("/deleteuser/{user.id}")
async def delete_user(user_id: int):
    for user in users_db:
        if user_id == user.id:
            users_db.pop(user)
            return {'message': 'User deleted'}
    raise HTTPException(status_code=400, detail="User not found")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
