from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.auth import
from db.session import Base, engine, SessionLocal
from schemas.user import UserLogin
from schemas.token import Token
from utils import verify_password
from core.security import create_acess_token, decode_access_token

auth_router = APIRouter(prefix='/auth', tags=['auth'])

