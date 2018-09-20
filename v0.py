import inotify.adapters
import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')
FOLDER = os.getenv('FOLDER', '/tmp')
EXTENSION = os.getenv('EXTENSION', 'mp4')
DESTINATION = os.getenv('DESTINATION')

bot = telebot.TeleBot(TOKEN)
notifier = inotify.adapters.Inotify()
notifier.add_watch(FOLDER)

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CREATE' in event[1] and EXTENSION + '.' not in event[3]:
            bot.send_animation(DESTINATION, event[3])
