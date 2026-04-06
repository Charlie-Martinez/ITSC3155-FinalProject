from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class RatingBase(BaseModel):
    customer_id: int
    order_id: int
    rating: int
    review_text: Optional[str] = None

class RatingCreate(RatingBase):
    pass

class RatingUpdate(BaseModel):
    customer_id: Optional[int] = None
    order_id: Optional[int] = None
    rating: Optional[int] = None
    review_text: Optional[str] = None

class Rating(RatingBase):
    id: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True
