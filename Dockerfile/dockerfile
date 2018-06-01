FROM python:3.6 AS base
MAINTAINER wwb
EXPOSE 80

WORKDIR /app
COPY ./src requirement.txt install.sh ./
RUN sh +x install.sh
ENTRYPOINT [ "python","server.py" ]