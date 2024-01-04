FROM python:3.7-slim-buster

RUN apt update -y && apt upgrade -y
RUN apt install ffmpeg -y

COPY ./app /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt