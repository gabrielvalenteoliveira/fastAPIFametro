from sqlalchemy.orm import Session
from sqlalchemy import select
from models.company import Company
from schemas.company import CompanyCreate
from fastapi import HTTPException, status

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(
        cnpj=company.cnpj, 
        razao_social=company.razao_social,
        orgao = company.orgao,
        city = company.city,
        state = company.state
        )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def delete_company(db: Session, company_id: int):
    db_company = db.query(Company).filter(Company.user_id == company_id).first()

    if db_company:
        db.delete(db_company)
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="Company not found")