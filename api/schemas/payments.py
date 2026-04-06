
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    card_number: str
    card_holder: str
    expiration_date: str
    payment_type: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_number: Optional[str] = None
    card_holder: Optional[str] = None
    expiration_date: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None


class Payment(PaymentBase):
    id: int
    transaction_status: str
    transaction_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
