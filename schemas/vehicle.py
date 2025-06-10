from pydantic import BaseModel, Field

class VehicleCreate(BaseModel):
    plate: str
    model: str
    vehicle_year: int = Field(..., ge=1900, le=2100)
    renavam: int 
    brand: str

class VehicleOut(BaseModel):
    plate: str
    model: str
