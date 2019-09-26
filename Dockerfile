FROM python:3.6.8

MAINTAINER Victor Danila

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

ADD . /app