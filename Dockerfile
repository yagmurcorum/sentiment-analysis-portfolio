# Python 3.9 slim imajını kullan
FROM python:3.9-slim

# Çalışma dizinini belirle
WORKDIR /app

# Gerekli dosyaları kopyala
COPY requirements.txt .
COPY main.py .
COPY app.py .

# Sistem bağımlılıklarını kur
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python kütüphanelerini kur
RUN pip install --no-cache-dir -r requirements.txt

# Port 8000'i aç
EXPOSE 8000

# Uygulamayı başlat
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]