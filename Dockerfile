FROM python:3.7-alpine

RUN pip install pytelegrambotapi
RUN pip install inotify

ADD file2gif.py / 

CMD [ "python", "./file2gif.py" ]
