from sqlalchemy import Column, String, Integer, Date
from db.session import Base

class Vehicle(Base):
    __tablename__: 'Vehicles'

    Fk = Column()
    Plate = Column(String, nullable=False, primary_key=True)
    Model = Column(String, nullable=False)
    Year = Column(Date, nullable=False)