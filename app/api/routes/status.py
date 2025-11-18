"""Health and status endpoints."""

from fastapi import APIRouter

router = APIRouter(tags=["status"])


@router.get("/status")
async def status():
    return {"ok": True, "service": "Permis de Conduire Maroc API"}


