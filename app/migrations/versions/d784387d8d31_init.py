"""init

Revision ID: d784387d8d31
Revises: 
Create Date: 2025-05-11 16:00:41.452164

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import TIMESTAMP

# revision identifiers, used by Alembic.
revision: str = 'd784387d8d31'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.BigInteger(), autoincrement=True, primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("surname", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=100), nullable=False),


        # Используем TIMEZONE('utc', CURRENT_TIMESTAMP) вместо NOW()
        # Это гарантирует запись времени в UTC независимо от настроек сервера БД
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
            nullable=False
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
            onupdate=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
            nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("user")
