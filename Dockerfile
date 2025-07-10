FROM python:3.10-slim-buster

# Install required packages
RUN apt-get update -y && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by the Flask app (default: 8080)
EXPOSE 8080

# Run the app
CMD ["python3", "app.py"]
