from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.sql import func

from app.database.connection import Base


class Sneaker(Base):
    __tablename__ = "sneakers"

    id = Column(Integer, primary_key=True, index=True)

    brand = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    sku = Column(String(50), unique=True, index=True)
    colorway = Column(String(150))

    release_date = Column(Date)

    retail_price = Column(Float)

    gender = Column(String(20))

    image_url = Column(String(500))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )