from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Default App Title'
    app_description: Optional[str] = None
    database_url: str
    secret_key: str = 'debug_secret_key'

    class Config:
        env_file = '.env'


settings = Settings()