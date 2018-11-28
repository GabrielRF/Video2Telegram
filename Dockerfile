FROM python:3.7-alpine

RUN apk --no-cache --virtual build add build-base libffi-dev openssl-dev && rm -rf ~/.pip/ 
RUN pip install python-telegram-bot
RUN pip install inotify
RUN pip install moviepy
RUN apk del build

ADD file2gif.py / 

CMD [ "python", "./file2gif.py" ]
