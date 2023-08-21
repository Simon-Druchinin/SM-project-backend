import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()

@dataclass
class SMTPConfig:
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str

@dataclass
class RedisConfig:
    HOST: str
    PORT: int

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
    redis: RedisConfig
    smtp: SMTPConfig

SECRET_AUTH=os.environ.get('SECRET_AUTH')

config = Config(
    db=DBConfig(
        HOST=os.environ.get("DB_HOST"),
        PORT=os.environ.get("DB_PORT"),
        PASSWORD=os.environ.get("DB_PASS"),
        USER=os.environ.get("DB_USER"),
        NAME=os.environ.get("DB_NAME"),
    ),
    redis=RedisConfig(
        HOST=os.environ.get("REDIS_HOST"),
        PORT=os.environ.get("REDIS_PORT"),
    ),
    smtp=SMTPConfig(
        HOST=os.environ.get("SMTP_HOST"),
        PORT=os.environ.get("SMTP_PORT"),
        USER=os.environ.get("SMTP_USER"),
        PASSWORD=os.environ.get("SMTP_PASS"),
    ),
)
