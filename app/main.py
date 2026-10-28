from fastapi import FastAPI
from app.presentation.api.v1.users import router as users_router

app = FastAPI(
    title="Clean Architecture FastAPI Service",
    description="Domain-Driven Design (DDD) & Clean Architecture Template",
    version="1.0.0"
)

app.include_router(users_router, prefix="/api/v1")

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "healthy", "architecture": "clean_ddd"}
