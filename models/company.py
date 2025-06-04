from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from datetime import datetime
from db.session import Base


class Company(Base):
    __tablename__ = 'Company'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('User.id'))
    cnpj = Column(String, nullable=False)
    razao_social = Column(String, nullable=False)
    orgao = Column(String, default=None)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    