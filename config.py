from pydantic import BaseSettings

class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port:int = 8000
    debug_mode: bool
    log_level: str = 'info'
    
    class Config:
        env_file = '.env'
