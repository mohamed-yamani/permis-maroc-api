"""Route registration helpers."""

from fastapi import FastAPI

from app.api.routes.status import router as status_router


def register_routes(app: FastAPI) -> None:
    """Include all routers on the FastAPI app."""
    app.include_router(status_router)


