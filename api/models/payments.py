from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    card_number = Column(String(20), nullable=False)
    card_holder = Column(String(100), nullable=False)
    expiration_date = Column(String(10), nullable=False)
    transaction_status = Column(String(30), nullable=False, default="Pending")
    payment_type = Column(String(30), nullable=False)
    transaction_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    order = relationship("Order", back_populates="payment")