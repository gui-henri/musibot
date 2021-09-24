from __future__ import unicode_literals
import youtube_dl
import os
import html
import time

class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def ydl_hook(d):
    if d['status'] == 'finished':
        print('Download finalizado, convertendo ...')


def download_music(video_id):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '.cache/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        }],
        'logger': Logger(),
        'progress_hooks': [ydl_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v={}'.format(video_id)])

