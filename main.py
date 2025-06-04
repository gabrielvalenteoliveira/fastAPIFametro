import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints.user import user_router
from api.v1.endpoints.vehicle import vehicle_router
from api.api.endpoints.company import company_router
from fastapi import FastAPI
from db.session import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)