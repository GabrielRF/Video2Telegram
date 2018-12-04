import inotify.adapters
import os
import telegram
import ffmpy

TOKEN = os.getenv('BOT_TOKEN')
FOLDER = os.getenv('FOLDER', '/tmp/')
EXTENSION = os.getenv('EXTENSION', 'mp4')
DESTINATION = os.getenv('DESTINATION')
SPEEDX = os.getenv('SPEEDX',2)
RESIZE = os.getenv('RESIZE',0.8)
FPS = os.getenv('FPS',5)

bot = telegram.Bot(TOKEN)
notifier = inotify.adapters.InotifyTree(FOLDER)

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CLOSE_WRITE' in event[1] and EXTENSION in event[3]:
            file_path = event[2] + '/' + event[3]
            try:
                gif_path = '/tmp/file2gif.gif'
                ff = ffmpy.FFmpeg(
                    inputs={file_path: None},
                    outputs={gif_path: None}
                )
                ff.run()
                file_open = open(gif_path, 'rb')
                bot.send_chat_action(DESTINATION, 'upload_video')
                bot.send_animation(DESTINATION, file_open, timeout=300)
            except:
                file_open = open(file_path, 'rb')
                bot.send_chat_action(DESTINATION, 'upload_document')
                bot.send_document(DESTINATION, file_open, timeout=600)
