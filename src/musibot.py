import pygame
import json
from lib.MusiBotPlayer import MusiBotPlayer
from services.youtubedl import download_music
from services.youtubeApi import search_music_to_download
import utils.musibotUtils as utils
from utils.menuHandler import main_menu

CACHE_DIR = '.cache/'

musibot = MusiBotPlayer()

while musibot.running:
    utils.clear_terminal()
    utils.setup_cache_files(CACHE_DIR)

    with open(CACHE_DIR + 'playlist.json') as f:
        musibot.play_list_data = json.load(f)

        if musibot.play_list_data.get("playlist") == []:
            mus_name = input('Não há músicas na lista de reprodução. Adicione uma ou digite Q para sair: ')
            
            if mus_name == 'Q' or mus_name == 'q':
                musibot.running = False
                break

            musibot.add_to_playlist(mus_name)

        musibot.load_and_play(CACHE_DIR + musibot.play_list_data['playlist'][0])

        main_menu(musibot)

        utils.delete_file('{0}{1}'.format(CACHE_DIR, musibot.play_list_data['playlist'][0]))
        musibot.remove_from_playlist(0) 

    with open('.cache/playlist.json', 'w') as f:
        json.dump(musibot.play_list_data, f)
