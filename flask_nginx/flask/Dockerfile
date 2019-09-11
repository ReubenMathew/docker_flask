FROM python:3.7.2-stretch

MAINTAINER Reuben Ninan "reubenninan@outlook.com"

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install uwsgi

CMD ["uwsgi", "app.ini"]
