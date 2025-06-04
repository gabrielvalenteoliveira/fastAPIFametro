from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.user import VehicleCreate
from services.vehicle import create_vehicle, read_vehicles, delete_vehicle

company_router = APIRouter(prefix='/company', tags=["company"])

