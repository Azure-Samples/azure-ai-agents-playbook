FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY 05-orchestrated-agents-with-custom-openapi-tools/aci_requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r aci_requirements.txt

# Copy the FastAPI application
COPY 05-orchestrated-agents-with-custom-openapi-tools/bank_transactions_api.py .

# Expose the port the app runs on
EXPOSE 80

# Command to run the application
# Use environment variable for port with default value
ENV PORT=80
CMD ["sh", "-c", "python bank_transactions_api.py $PORT"]