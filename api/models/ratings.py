from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    rating = Column(Integer, nullable=False)
    review_text = Column(String(1000), nullable=True)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())

    customer = relationship("Customer", back_populates="ratings")
    order = relationship("Order")