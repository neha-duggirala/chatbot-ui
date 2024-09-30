# Project Highlights

## 1. Using Poetry Instead of the Old School `requirements.txt` Method

**Pros:**
- Dependency Management: Poetry handles dependency resolution more effectively, ensuring that all dependencies are compatible.
- Environment Isolation: It creates a virtual environment automatically, which helps in maintaining a clean workspace.
- Project Metadata: Poetry allows you to manage project metadata (like version, description, etc.) in a single `pyproject.toml` file.
- Publishing: It simplifies the process of publishing packages to PyPI.
- Lock File: Generates a `poetry.lock` file, which ensures reproducible builds by locking the exact versions of dependencies.

**Cons:**
- Learning Curve: It might have a steeper learning curve for those used to `requirements.txt`.
- Compatibility: Some legacy projects or tools might not fully support Poetry.
- Overhead: For very simple projects, Poetry might feel like overkill.

## 2. Added Multi-Stage Build While Building Dockerfile

**Pros:**
- Reduced Image Size: Multi-stage builds help in creating smaller Docker images by only including necessary components.
- Improved Security: Smaller images have fewer vulnerabilities.
- Faster Builds: By using caching effectively, it speeds up the build process.
- Cleaner Images: Helps in keeping the final image clean and free from build dependencies.

**Cons:**
- Complexity: Multi-stage builds can make Dockerfiles more complex and harder to read.
- Debugging: Debugging issues in multi-stage builds can be more challenging.
- Build Time: Initial build times might be longer due to the additional stages, though subsequent builds will be faster.
