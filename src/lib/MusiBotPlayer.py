import pygame

from services.youtubedl import download_music
from services.youtubeApi import search_music_to_download

class MusiBotPlayer:

    def __init__(self, running = True, play_list_data = None):

        self.running = running
        self.play_list_data = play_list_data

        pygame.init()
        pygame.mixer.init()
    
    def add_to_playlist(self, mus_name):
        video_data = search_music_to_download(mus_name)
        download_music(video_data['videoId'])
        self.play_list_data['playlist'].append(video_data['videoId'] + '.wav')

    def remove_from_playlist(self, index):
        del self.play_list_data['playlist'][index]
    
    def load_and_play(self, file_name):
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()
    def unpause(self):
        pygame.mixer.music.unpause()
    def stop(self):
        pygame.mixer.music.stop()
    def restart(self):
        pygame.mixer.music.play()
    def is_playing(self):
        return pygame.mixer.music.get_busy()