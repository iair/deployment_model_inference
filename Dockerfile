# Use an official Python image
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy the entire project directory
COPY . /app/

# Install dependencies without creating a virtual environment
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Command to run the inference script
CMD ["poetry", "run", "python", "src/inference.py"]