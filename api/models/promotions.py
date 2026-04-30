from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, Boolean, func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(50), unique=True, nullable=False)
    expiration_date = Column(DATETIME, nullable=False)
    discount_type = Column(String(20), nullable=False, default='percentage')
    discount_value = Column(DECIMAL(10, 2), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DATETIME, server_default=func.now())

    order = relationship("Order", back_populates="promotion")