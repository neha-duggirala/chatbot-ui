
### Use Case
You have a Streamlit chatbot that you want to containerize and share with a friend.


### Features

1. ***User Input Logging:***  The application captures and records user interactions for later analysis or debugging.
2. ***Chatbot Functionality:*** user inputs are processed, and responses are generated and displayed.

### Steps
1. **Create Dockerfile**
2. **Build Docker Image**
    `docker build -t your_image_name .`
3. **Run Docker Image**
    `docker run -p local_port:container_port your_image_name`
4. Verify the Streamlit application is running by accessing the mapped port.

### Observed Problems
1. **Rebuilding Time**: Every change triggers reinstallation of all requirements, increasing build time.
2. **Image Size**: The Docker image is too large, contradicting the goal of creating a lightweight application.

### Solutions
1. **Docker's Caching Mechanism**: Did not help.
2. **Base Layer Reduction**: Switching from `python:3.10` to `python:3.9-slim` reduced the image size.
3. **Using Poetry**: Helps avoid dependency errors and simplifies dependency management compared to `requirements.txt`.
4. **Multi-Stage Builds**: Keeps only necessary artifacts in the final image.

### Multi-Stage Build Example
```dockerfile
# Stage 1: Build
FROM python:3.9-alpine as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /app /app
COPY . .
```

### To Do
1. **Use Poetry**: [YouTube Tutorial](https://www.youtube.com/watch?v=Ji2XDxmXSOM&t=50s)
2. **Understand Multi-Stage Builds**
