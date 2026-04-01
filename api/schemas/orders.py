from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail
from .customers import Customer
from .promotions import Promotion



class OrderCreate(BaseModel):
    customer_name: str
    description: Optional[str] = None
    tracking_number: str
    delivery_type: str
    total_price: float
    customer_id: int
    promotion_id: Optional[int] = None


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    delivery_type: Optional[str] = None
    total_price: Optional[float] = None
    customer_id: Optional[int] = None
    promotion_id: Optional[int] = None


class Order(OrderCreate):
    id: int
    order_date: datetime
    order_status: str
    order_details: list[OrderDetail] = None
    customer: Optional[Customer] = None
    promotion: Optional[Promotion] = None

    class ConfigDict:
        from_attributes = True
