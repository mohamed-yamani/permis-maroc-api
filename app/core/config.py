"""Application configuration and settings."""

from pydantic import BaseModel


class Settings(BaseModel):
    APP_NAME: str = "Permis de Conduire Maroc API"


settings = Settings()


