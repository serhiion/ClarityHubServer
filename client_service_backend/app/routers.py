from fastapi import APIRouter

client_service_backend_router = APIRouter()

@client_service_backend_router.get("/")
async def root():
    return {"message": "Hello from ClarityHubServer!"}