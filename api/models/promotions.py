from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(50), unique=True, nullable=False)
    discount_percent = Column(DECIMAL(5, 2), nullable=False)
    expiration_date = Column(DATETIME, nullable=False)

    order = relationship("Order", back_populates="promotion")