# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Current directory that Dockerfile is in is copied to app directory in container
COPY . /Application
WORKDIR /Application
RUN pip install -r requirements.txt

#EXPOSE 3000

# Pipiline commands
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
