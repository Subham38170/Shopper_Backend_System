from pydantic_settings import BaseSettings,SettingsConfigDict


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)



class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITH: str
    


    model_config =SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )