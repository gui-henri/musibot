import os
import os.path
from os import path

def clear_terminal():
    print("\n" * 130)

def create_playlist(playlist_dir):
    f = open(playlist_dir + 'playlist.json', 'a')
    f.write('{"playlist": []}')
    f.close()

def setup_cache_files(p_cache_dir):
    if not path.exists(p_cache_dir):
        os.mkdir(p_cache_dir)
        
        create_playlist(p_cache_dir)
    
    if not path.exists(p_cache_dir + 'playlist.json'):
        create_playlist(p_cache_dir)
def delete_file(file_dir):
    os.remove(file_dir)