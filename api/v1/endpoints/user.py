from fastapi import FastAPI, HTTPException
from schemas.user import UserCreate, UserOut
from crud.user import get_user_by_email, create_user
from typing import List
import uvicorn

app = FastAPI()

@app.post("/register/", response_model=UserCreate)
async def create_user(user: User) -> User:

    return user

@app.get("/users/", response_model=List[User])
async def read_users() -> List[User]:
    return users_db

@app.put("/updateuser/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User) -> User:

    raise HTTPException(status_code=400, detail="User not found")


@app.delete("/deleteuser/{user.id}")
async def delete_user(user_id: int):

    raise HTTPException(status_code=400, detail="User not found")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
