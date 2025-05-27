from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from schemas.user import UserCreate
from utils import hash_password
from fastapi import HTTPException, status

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(user: UserCreate, db: Session):
        hashed_password = hash_password(user.password)
        db_user = User(
            name=user.name, 
            hashed_password=hashed_password,
            email=user.email,
            cpf=user.cpf,
            phone=user.phone,
            birthdate=user.birthdate,
            is_admin=user.is_admin
            )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

def get_all_users(db: Session):
    query = select(User)
    result = db.execute(query)
    users = result.scalars().all()

    return users

def update_user(db: Session, user_id: int, user_data: UserCreate):
    user_to_update = db.query(User).filter(User.id == user_id).first()

    if user_to_update:
        if user_data.name is not None:
            user_to_update.name = user_data.name
        if user_data.password is not None:
            user_to_update.hashed_passwordpassword = hash_password(user_data.password)
        if user_data.email is not None:
            user_to_update.email = user_data.email
        if user_data.cpf is not None:
            user_to_update.cpf = user_data.cpf
        if user_data.phone is not None:
            user_to_update.phone = user_data.phone
        if user_data.birthdate is not None:
            user_to_update.birthdate = user_data.birthdate

        db.commit()
        db.refresh(user_to_update)
    else:
        raise HTTPException(status_code=400, detail="User not found")
    
    return user_to_update

def delete_user(db: Session, user_id: int):
    deleted_user = db.query(User).filter(User.id == user_id).first()

    if deleted_user:
        db.delete(deleted_user)
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="User not found")
