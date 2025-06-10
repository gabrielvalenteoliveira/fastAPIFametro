from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from services.auth import get_current_user, get_user, user_is_admin
from sqlalchemy.orm import Session
from core.security import create_acess_token
from utils import verify_password
from db.session import Base, engine, SessionLocal
from schemas.user import UserLogin
from schemas.token import Token
from utils import verify_password
from core.security import create_acess_token, decode_access_token

auth_router = APIRouter(prefix='/auth', tags=['auth'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNATHOURIZED,
            detail="Credenciais incorretas", 
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_acess_token(data={"sub": user.name, "is_admin": user.is_admin})
    return {"access_token": access_token, "token_type": "bearer"}


