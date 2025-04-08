FROM python:3.11-slim

# и так ясно
WORKDIR /app

# установка requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копировать все 
COPY . .

# запускаем приложение
CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
