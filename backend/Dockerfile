# Базовый образ
FROM python:3.9-slim

# Установи рабочую директорию
WORKDIR /app

# Скопируй зависимости и установи их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируй весь код
COPY . .

RUN flask db upgrade

# Открой порт 5000
EXPOSE 5000

# Запусти Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
