from typing import Optional
from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    phone: str
    address: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None

class Customer(CustomerBase):
    id: int
    class ConfigDict:
        from_attributes = True
