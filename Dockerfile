FROM python:3.7-alpine

RUN pip install python-telegram-bot
RUN pip install inotify
RUN pip install moviepy

ADD file2gif.py / 

CMD [ "python", "./file2gif.py" ]
