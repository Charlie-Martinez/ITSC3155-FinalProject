from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    order_id: int
    payment_method: str
    transaction_status: str
    masked_card_info: Optional[str] = None
    amount: float

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    payment_method: Optional[str] = None
    transaction_status: Optional[str] = None
    masked_card_info: Optional[str] = None
    amount: Optional[float] = None

class Payment(PaymentBase):
    id: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True
