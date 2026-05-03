from typing import Optional
from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    phone: str
    address: str
    email: str

CustomerCreate = CustomerBase

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True