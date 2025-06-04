from pydantic import BaseModel

class VehicleCreate(BaseModel):
    plate: str
    model: str
    year: str
    renavam: int 
    brand: str

class VehicleOut(BaseModel):
    plate: str
    model: str
