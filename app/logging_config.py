from loguru import logger
import sys

# Аскетичная настройка логера.

# Путь к лог-файлу
LOG_FILE = "./logs/app.log"

# Очистка стандартных хендлеров
logger.remove()

# Логирование в консоль
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan> - {message}",
    level="DEBUG",
)

# Логирование в файл
logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="7 days",
    compression="zip",
    enqueue=True,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function} | {message}",
)

def get_logger():
    return logger