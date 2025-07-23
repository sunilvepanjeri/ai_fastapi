from pydantic_settings import BaseSettings
import os
from enum import Enum
from dotenv import find_dotenv


class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"



class Settings(BaseSettings):
    openai_api_key: str

    model_config = {"extra": "allow"}




keys = Settings(_env_file = find_dotenv(".env"))


os.environ.update(keys.model_dump())