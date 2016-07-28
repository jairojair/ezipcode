FROM python:3.5-alpine

MAINTAINER jairojair@gmail.com

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt
