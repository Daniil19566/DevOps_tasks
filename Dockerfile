# Базовый образ
FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Команда по умолчанию (замени на свою)
CMD ["python", "main.py"]
