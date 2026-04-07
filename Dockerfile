# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .
RUN mkdir -p /app/instance && chmod -R 777 /app/instance
# Expose port
EXPOSE 5000

# Run app
CMD ["python", "run.py"]