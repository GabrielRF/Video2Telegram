import inotify.adapters
import os
import telegram
from moviepy.editor import *

TOKEN = os.getenv('BOT_TOKEN')
FOLDER = os.getenv('FOLDER', '/tmp/')
EXTENSION = os.getenv('EXTENSION', 'mp4')
DESTINATION = os.getenv('DESTINATION')

bot = telegram.Bot(TOKEN)
notifier = inotify.adapters.InotifyTree(FOLDER)

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CLOSE_WRITE' in event[1] and EXTENSION in event[3]:
            file_path = event[2] + '/' + event[3]
            file_open = open(file_path, 'rb')
            try:
                bot.send_animation(DESTINATION, file_open)
            except:
                bot.send_document(DESTINATION, file_open)
