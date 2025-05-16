from fastapi import APIRouter, Depends
from services.user import get_user_by_email, create_user, get_all_users, update_user, delete_user
from core.security import create_acess_token, decode_access_token
from db.session import Base, engine, SessionLocal
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

@user_router.post("/register/", status_code=HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
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
    return create_user(db, user)        

@user_router.post("/login", response_model=UserOut)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    return 


@user_router.get("/get_users/")
async def read_users(db: Session = Depends(get_db)) -> List[User]:
    return get_all_users(db)



@user_router.put("/updateuser/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_data)


@user_router.delete("/deleteuser/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)


