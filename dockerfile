# Stage 1: Install dependencies
FROM python:3.9-slim AS builder

# Set the working directory in the container
WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install
RUN poetry shell

# Stage 2: Copy dependencies and application code
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies from the builder stage
COPY -from=builder /app/.venv /app/.venv

# Copy the application code
COPY . .
# Set the environment variable to use the virtual environment
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches
CMD ["streamlit", "run", "main.py"]