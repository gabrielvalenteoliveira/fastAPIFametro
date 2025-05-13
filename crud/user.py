from sqlalchemy.orm import Session
from models.user import User
from schemas import UserCreate
from utils import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, hashed_password=hashed_pw, cpf=user.cpf, phone=user.phone, birthdate=user.birthdate)
    db.add()
    db.commit()
    db.refresh(new_user)
    return new_user