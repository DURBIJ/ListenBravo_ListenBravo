# Dockerfile for building the FastAPI project

# Start with an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install poetry
RUN pip install poetry

# Install dependencies from pyproject.toml
RUN poetry install

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
