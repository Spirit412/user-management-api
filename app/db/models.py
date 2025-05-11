from datetime import datetime, timezone

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa

class User(BigIntAuditBase):
    __tablename__ = "user"

    name: Mapped[str] = Column("name", String(100))
    surname: Mapped[str] = Column("surname", String(100))
    password: Mapped[str] = Column("password", String(100))
    # Явное указание UTC для created_at
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
        default=lambda: datetime.now(timezone.utc)
    )

    # Явное указание UTC для updated_at
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
        onupdate=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
        default=lambda: datetime.now(timezone.utc)
    )
