FROM python:latest

RUN apt update \ 
    && apt install git -y \ 
    && apt install vim -y

WORKDIR /var/www
RUN pip install --upgrade pip && pip install django
RUN django-admin startproject soninet

WORKDIR /var/www/soninet
