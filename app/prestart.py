import asyncio
import logging
from alembic import command
from alembic.config import Config
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine
from app.config import get_settings
from app.db.session import sqlalchemy_config
from app.logging_config import get_logger

settings = get_settings()
logger = get_logger()

def apply_migrations():
    """миграции Alembic."""
    try:
        logger.info("Применение миграций...")
        alembic_cfg = Config("app/alembic.ini")
        command.upgrade(alembic_cfg, "head")
        logger.info("Миграции успешно применены.")
    except Exception as e:
        logger.critical(f"Ошибка применения миграций: {e}", exc_info=True)
        raise

async def check_db_connection():
    """Проверяет подключение к БД."""
    try:
        logger.info("Проверка подключения к БД...")
        engine = sqlalchemy_config.get_engine()
        if not isinstance(engine, AsyncEngine):
            raise TypeError("Неподдерживаемый тип движка")

        async with engine.begin() as conn:
            result = await conn.execute(text("SELECT 1"))
            logger.info(f"Подключение к БД успешно: {result.scalar()}")
    except Exception as e:
        logger.critical(f"Ошибка подключения к БД: {e}", exc_info=True)
        raise

async def run_checks():
    """все предварительные проверки."""
    apply_migrations()
    await check_db_connection()

if __name__ == "__main__":
    asyncio.run(run_checks())