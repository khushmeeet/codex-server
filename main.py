from fastapi import FastAPI
import uvicorn
from config import Settings
from apps.default.routes import r

settings = Settings()

app = FastAPI()

app.include_router(r, prefix='/d')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.host,
        port=settings.port,
        reload=settings.debug_mode,
        log_level=settings.log_level
    )