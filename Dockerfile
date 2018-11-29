# FROM debian:jessie-slim
FROM ubuntu:bionic

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python
RUN apt-get -y install build-essential libssl-dev libffi-dev python-dev
RUN apt-get -y install python-pip
RUN apt-get -y install ffmpeg
RUN pip install --upgrade setuptools
RUN pip install python-telegram-bot
RUN pip install inotify
RUN pip install requests
RUN pip install moviepy

ADD file2gif.py /

CMD [ "python", "./file2gif.py" ]
