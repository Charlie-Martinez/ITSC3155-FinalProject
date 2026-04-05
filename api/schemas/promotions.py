from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PromotionBase(BaseModel):
    promo_code: str
    discount_type: str
    discount_value: float
    expiration_date: datetime
    is_active: bool

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None
    expiration_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class Promotion(PromotionBase):
    id: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True
