import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.base import Base


class Sneaker(Base):
    __tablename__ = "sneakers"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    brand = Column(
        String(50),
        nullable=False,
        index=True
    )

    model = Column(
        String(100),
        nullable=False
    )

    sku = Column(
        String(50),
        nullable=False,
        unique=True,
        index=True
    )

    colorway = Column(String(150))

    gender = Column(String(20))

    release_date = Column(Date)

    retail_price = Column(Numeric(10, 2))

    currency = Column(
        String(3),
        nullable=False,
        default="USD"
    )

    image_url = Column(String(500))

    is_active = Column(
        Boolean,
        nullable=False,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )