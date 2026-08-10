FROM python:3.11-slim

WORKDIR /app

# Install dependencies first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and group
RUN adduser --disabled-password --gecos "" appuser

# Copy only the necessary application source code and frontend
COPY app/ ./app
COPY frontend/ ./frontend

# Set ownership of the application directory
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]