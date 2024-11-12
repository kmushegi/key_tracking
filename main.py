from fastapi import FastAPI
from routes.key_routes import router as key_router
from routes.webhook_routes import router as webhook_router
from database import connect_db, close_db

app = FastAPI(title="Key Tracking System")


# Database connection
@app.on_event("startup")
async def startup_db_client():
    connect_db()


@app.on_event("shutdown")
async def shutdown_db_client():
    close_db()


# Registering routers
app.include_router(key_router, prefix="/keys", tags=["Keys"])
app.include_router(webhook_router, prefix="/webhooks", tags=["Webhooks"])
