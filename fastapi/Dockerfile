# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Installl dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8200

# Command to run the server
CMD ["uvicorn", "iris_fast_api:app", "--host", "0.0.0.0", "--port", "8200"]
