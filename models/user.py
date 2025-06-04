from sqlalchemy import Column, Integer, String, Date, Boolean, ForegnKe
from datetime import datetime
from db.session import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date, default=datetime.utcnow)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    phone = Column(String, unique=True)
    birthdate = Column(Date, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)