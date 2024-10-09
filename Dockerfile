# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Set PYTHONPATH so tests can find the main module
ENV PYTHONPATH=/app

CMD ["pytest", "tests"]
