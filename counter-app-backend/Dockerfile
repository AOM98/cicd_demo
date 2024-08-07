# Use the official Python image from the Python 3.12 documentation
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install FastAPI and Uvicorn
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
