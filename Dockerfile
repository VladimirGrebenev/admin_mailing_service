FROM python:3.10

# Установка Redis
RUN apt-get update && apt-get install -y redis-server

# Установка Postgres
RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

# Обновление PIP
RUN pip3 install --upgrade pip

# Назначение рабочей директории в контейнере
WORKDIR /app

# Копирование файлов и установка зависимостей
COPY ./admin_mailing/ ./
RUN pip3 install -r requirements.txt

# Запуск скрипта ожидающего старта базы данных
COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

# Запуск Redis сервера
CMD redis-server &

# Запуск Celery worker и Celery beat
CMD celery -A admin_mailing worker --loglevel=info && celery -A admin_mailing beat

# установка gunicorn для боевого подкоючения
RUN pip3 install gunicorn