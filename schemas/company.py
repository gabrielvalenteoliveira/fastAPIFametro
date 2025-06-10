from pydantic import BaseModel, EmailStr

class CompanyCreate(BaseModel):
    razao_social: str
    cnpj: str
    orgao: str
    city: str
    state: str

class CompanyOut(BaseModel):
    cnpj: str
    razao_social: str
    user_id: int

    class Config:
        orm_mode = True
