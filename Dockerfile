FROM python:3.9-buster

RUN pip install flask
RUN mkdir /src
WORKDIR /src
