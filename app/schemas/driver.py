
from pydantic import BaseModel


class Driver(BaseModel):
    id: str
    first_name: str
    last_name: str
    license_number: str
    status: str