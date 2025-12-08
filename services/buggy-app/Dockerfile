# Use a lightweight Python base image
FROM python:3.9-slim

# Prevent Python from buffering stdout/stderr (Good for logs)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (Caching layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run the app
CMD ["python", "main.py"]