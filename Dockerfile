FROM python:3.12

# system deps for common DB/files or static serving
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# create DB (non-blocking) - safe if DB already exists
RUN python init_db.py || true

EXPOSE 5000

# Use gunicorn for a multi-worker, production-like server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "hangman:app", "--workers", "2", "--timeout", "30"]
