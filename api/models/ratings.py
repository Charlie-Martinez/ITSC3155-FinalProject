from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    score = Column(Integer, nullable=False)
    review_text = Column(String(1000), nullable=True)
    review_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    customer = relationship("Customer", back_populates="ratings")