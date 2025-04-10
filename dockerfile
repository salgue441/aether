FROM python:3.10-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install -e .

# Set command to run when the container starts
ENTRYPOINT ["aether"]
CMD ["--help"]

# Development image
FROM base as dev

# Install development dependencies
RUN pip install -e ".[dev]"

# Testing image
FROM base as test

# Install test dependencies
RUN pip install -e ".[dev]"

# Run tests
CMD ["pytest"]
