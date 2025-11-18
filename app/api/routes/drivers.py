from fastapi import APIRouter
from app.schemas import Driver


router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.get("/{driver_id}", response_model=Driver)
async def get_driver(driver_id: str):
    return Driver(
        id=driver_id,
        first_name="John",
        last_name="Doe",
        license_number="1234567890",
        status="active"
    )