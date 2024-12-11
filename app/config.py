from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    api_v1_prefix: str
    database_url: str

    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache
def get_settings() -> Settings:
    return Settings()