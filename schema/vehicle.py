from pydantic import BaseModel

class VehicleCreate(BaseModel):
    plate: str
    model: str
    year: str

class VehicleOut(BaseModel):
    plate: str

