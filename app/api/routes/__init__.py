"""Route registration helpers."""

from fastapi import FastAPI

from app.api.routes.status import router as status_router
from app.api.routes.license import router as license_router
from app.api.routes.drivers import router as drivers_router


def register_routes(app: FastAPI) -> None:
    """Include all routers on the FastAPI app."""
    app.include_router(status_router)
    app.include_router(license_router)
    app.include_router(drivers_router)


