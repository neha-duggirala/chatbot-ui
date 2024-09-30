
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


#### Stage 1: Builder Stage

- Base Image: Uses python:3.9-slim.
- Working Directory: Sets the working directory to /app.
- Copy Requirements: Copies only the requirements.txt file to leverage Docker cache.
- Install Dependencies: Installs the dependencies listed in requirements.txt.

#### Stage 2: Final Stage

- Base Image: Uses python:3.9-slim.
- Working Directory: Sets the working directory to /app.
- Copy Dependencies: Copies the installed dependencies from the builder stage.
- Copy Application Code: Copies the rest of the application code.
- Expose Port: Exposes port 8501 for Streamlit.
- Run Command: Sets the command to run the Streamlit application.


