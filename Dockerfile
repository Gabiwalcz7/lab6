FROM python:3.12-slim

WORKDIR /app

# instalacja zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# skopiowanie reszty plików (w tym app.py)
COPY . .

# komenda startowa – uruchamiamy naszą apkę
CMD ["python", "app.py"]
