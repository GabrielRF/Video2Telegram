#!/bin/sh

CONFIG_FILE=file2gif.py

if [ -z "$BOT_TOKEN" ]; then
    echo "Bot token missing."
    exit 1
else
    echo "Bot token present."
fi

if [ -z "$FOLDER" ]; then
    echo "Folder missing. Please, add the path where recording files are present."
    exit 1
else
    echo "Folder ok."
fi

if [ -z "$EXTENSION" ]; then
    echo "Recording file extension missing."
    exit 1
else
    echo "Extension ok."
fi

if [ -z "$DESTINATION" ]; then
    echo "Message destination missing."
    exit 1
else
    echo "Destination ok."
fi

/bin/cat <$CONFIG_FILE <<EOL
import inotify.adapters
import os
import telebot

notifier = inotify.adapters.Inotify()
notifier.add_watch('$FOLDER')
extension = '$EXTENSION'

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CREATE' in event[1] and extension not in event[3]:
print(event[3])
EOL
