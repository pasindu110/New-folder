FROM python:3.11-slim

# Install system dependencies (if needed for SQLite/Pillow)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libjpeg62-turbo-dev \
       zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency list first to leverage Docker layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Ensure start script is executable
RUN chmod +x start.sh

# Environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Expose the default port many PaaS providers use
EXPOSE 8080

# Default command: run init-if-needed then start Gunicorn
CMD ["sh", "-c", "./start.sh"]


