import inotify.adapters
import os

notifier = inotify.adapters.Inotify()
notifier.add_watch('/tmp')
extension = 'txt'

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CREATE' in event[1] and extension + '.' not in event[3]:
            print(event[3])
