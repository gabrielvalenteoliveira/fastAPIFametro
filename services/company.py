from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from schemas.user import UserCreate
from utils import hash_password
from fastapi import HTTPException, status