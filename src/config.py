import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()

@dataclass
class DBConfig:
    HOST: str
    PORT: int
    PASSWORD: str
    USER: str
    NAME: str

@dataclass
class Config:
    db: DBConfig

SECRET_AUTH=os.environ.get('SECRET_AUTH')

config = Config(
    db=DBConfig(
        HOST=os.environ.get("DB_HOST"),
        PORT=os.environ.get("DB_PORT"),
        PASSWORD=os.environ.get("DB_PASS"),
        USER=os.environ.get("DB_USER"),
        NAME=os.environ.get("DB_NAME"),
    ),
)
