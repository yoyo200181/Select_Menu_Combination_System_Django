# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.7
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

# create the app user
RUN useradd -m -s /bin/bash appuser && \
    mkdir -p /app/static && \
    chown appuser:appuser /app/static

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt


# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY . .

# Run the application.
RUN python3 src/manage.py collectstatic --noinput

# Expose the port that the application listens on.
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
