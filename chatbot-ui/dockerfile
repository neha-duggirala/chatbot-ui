# Stage 1: Install dependencies
FROM python:3.9-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

# Stage 2: Copy dependencies and application code
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY . .

# Set the environment variable to include Poetry's bin directory
ENV PATH="/root/.local/bin:$PATH"

# Expose the port that Streamlit uses
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "main.py"]