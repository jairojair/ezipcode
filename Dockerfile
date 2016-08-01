FROM python:3.5-alpine

MAINTAINER jairojair@gmail.com

RUN apk add --update \
	postgresql-dev \ 
	gcc \
	musl-dev \
	make

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt
