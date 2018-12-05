FROM ubuntu:bionic

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y python build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    python-pip \
    ffmpeg && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /tmp/*
RUN pip install --upgrade setuptools \
    python-telegram-bot \
    inotify \
    requests \
    ffmpy

ADD file2gif.py /

CMD [ "python", "./file2gif.py" ]
