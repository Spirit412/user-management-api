from advanced_alchemy.extensions.litestar import SQLAlchemySyncConfig
from app.config import get_settings

settings = get_settings()

# Конфиг для миграций
sqlalchemy_sync_config = SQLAlchemySyncConfig(
    connection_string=settings.DATABASE_URL.replace("+asyncpg", ""),  # меняем на sync драйвер
)