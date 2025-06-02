from fastapi import FastAPI

from client_service_backend.app.routers import client_service_backend_router

app = FastAPI()

app.include_router(client_service_backend_router)
