# Use an official Python image
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy only Poetry files first to leverage Docker caching
COPY pyproject.toml poetry.lock /app/

# Install dependencies (no virtual environment)
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the project files
COPY . /app

# Command to run the inference script
CMD ["poetry", "run", "python", "src/inference.py"]