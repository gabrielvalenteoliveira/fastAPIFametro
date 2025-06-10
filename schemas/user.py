from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    password: str
    cpf: str
    phone: str
    birthdate: str
    email: EmailStr
    is_admin: bool

class UserOut(BaseModel):
    name: str
    email: EmailStr
    id: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    hashed_password: str