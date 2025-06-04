from fastapi import APIRouter, Depends, status, HTTPException
from services.user import get_user_by_email, create_user, get_all_users, update_user, delete_user
from schemas.user import UserOut
from core.security import create_acess_token, decode_access_token
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.user import User
from schemas.user import UserCreate, UserOut, UserLogin
from utils import hash_password
from typing import List


user_router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if user.password:
        if len(user.password) <= 6:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="A sua senha deve ter mais de 6 caracteres"
            )
    db_name = db.query(User).filter(User.email == user.email).first()
    if db_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Nome já cadastrado, deseja fazer o login?"
        )
    db_cpf = db.query(User).filter(User.cpf == user.cpf).first()
    if db_cpf:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="CPF já cadastrado, deseja fazer o login?"
        )
    return create_user(user, db)


@user_router.get("/get_users")
async def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)



@user_router.put("/updateuser/{user_id}", response_model=UserOut)
async def update_a_user(user_id: int, updated_user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db, user_id, updated_user)


@user_router.delete("/deleteuser/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)


