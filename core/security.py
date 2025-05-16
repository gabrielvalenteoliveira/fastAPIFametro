from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "LAKSJ!)@(*&#@12398)ASDJKH!@390h1i230kJH12039hasd!@$))"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 30 

def create_acess_token(data: dict):
    to_encode = data.copy()
    expire = data.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.encode(token, SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        return None

