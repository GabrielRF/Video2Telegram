import inotify.adapters
import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')
FOLDER = os.getenv('FOLDER', '/tmp/')
EXTENSION = os.getenv('EXTENSION', 'mp4')
DESTINATION = os.getenv('DESTINATION')

bot = telebot.TeleBot(TOKEN)
notifier = inotify.adapters.InotifyTree(FOLDER)

bot.send_message(DESTINATION, 'Running')

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CLOSE_WRITE' in event[1] and EXTENSION in event[3]:
            file_path = event[2] + '/' + event[3]
            try:
                bot.send_video(DESTINATION, event[3])
            except:
                file_open = open(file_path, 'rb')
                bot.send_document(DESTINATION, file_open)
