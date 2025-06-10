from sqlalchemy.orm import Session
from schemas.user import UserLogin
from models.user import User
from sqlalchemy import select
from core.security import SECRET_KEY, ALGORITHM
from jose import JWTError, jwt
from utils import verify_password
from utils import hash_password
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(db: Session, username:str):
    user = db.query(User).filter(User.name == username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario não encontrado", 
        )
    return user
async def get_current_user(token: str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNATHOURIZED,
        detail="Token invalido",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        name: str = payload.get("sub")
        if name is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    user = get_user(name)
    if user is None:
        raise credentials_exception
    return user


async def user_is_admin(user: UserLogin = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Acesso restrito a administradores")
    return user

def user_is_admin(user):
    return user.is_admin