# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.7
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

#install psycopg2 dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y python3.8-dev python3-setuptools default-libmysqlclient-dev build-essential

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt


# Switch to the non-privileged user to run the application.
# USER appuser

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
# EXPOSE 8080

# # Run the application.
# CMD python3 ./src
