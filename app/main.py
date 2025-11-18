"""Application factory and FastAPI wiring."""

from fastapi import FastAPI

from app.api.routes import register_routes
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)
    register_routes(app)
    return app


