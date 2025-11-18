"""Health and license endpoints."""

from fastapi import APIRouter

router = APIRouter(tags=["license"])


@router.get("/license")
async def license():
    return {"ok": True, "license": "Permis de Conduire Maroc API"}



