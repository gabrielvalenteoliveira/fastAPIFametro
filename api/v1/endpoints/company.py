from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.company import CompanyCreate, CompanyOut 
from services.company import register_company, delete_company

company_router = APIRouter(prefix='/company', tags=["company"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@company_router.post('/create_company', status_code=status.HTTP_201_CREATED)
async def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return register_company(db, company)

@company_router.delete('/delete_company', status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(company_id: str, db: Session = Depends(get_db)):
    return delete_company(db, company_id)