from fastapi import FastAPI
import uvicorn
from config import Settings
from apps.web.routes import web
from mongoengine import connect, disconnect


settings = Settings()
app = FastAPI()
app.include_router(web, prefix='/web')


@app.on_event("startup")
async def startup_db_client():
    connect(host=settings.mongodb_uri)


@app.on_event("shutdown")
async def shutdown_db_client():
    disconnect()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.host,
        port=settings.port,
        reload=settings.debug_mode,
        log_level=settings.log_level
    )