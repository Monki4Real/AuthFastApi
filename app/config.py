from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):

    model_config = ConfigDict(
        env_file = '.env',
        env_file_encoding = 'utf-8',
        extra = 'ignore'
    )

    APP_NAME: str = 'Authentication'
    APP_VERSION: str = '0.0.1'
    DEBUG: bool = False

settings = Settings()   