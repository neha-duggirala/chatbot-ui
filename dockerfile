# Dockerfile example
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

# Install poetry and project dependencies
RUN pip install poetry\
    && poetry config virtualenvs.create false\
    && poetry install --no-interaction \
    && poetry install --no-root

# Copy the rest of your app
COPY . .

# Run the application (modify as needed)
CMD ["streamlit", "run", "main.py"]