FROM python:3.12-slim

WORKDIR /var/www/html

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/var/www/html

# Установка зависимостей
RUN pip install --upgrade pip && \
    pip install poetry==1.8.3

COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Копируем приложение в правильную структуру
#COPY ./app ./app/

# Команда должна совпадать с путями в контейнере
#CMD ["litestar", "--app", "app.main:app", "run", "--host", "0.0.0.0"]