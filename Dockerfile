# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Current directory that Dockerfile is in is copied to root in container
COPY . /Flask-Docker

WORKDIR /Flask-Docker

RUN pip install -r requirements.txt

# Pipiline commands
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

