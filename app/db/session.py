from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
)
from app.config import get_settings

settings = get_settings()
# Конфигурация БД
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.DATABASE_URL,
    before_send_handler="autocommit",
    session_config=AsyncSessionConfig(expire_on_commit=False),
    create_all=False,
)
