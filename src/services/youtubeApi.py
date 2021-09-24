from googleapiclient.discovery import build

YOUTUBE_API_KEY = 'REPLACE ME'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) 

def search_music_to_download(mus):
    search_response = youtube.search().list(
        q=mus,
        part='id,snippet',
        maxResults=1
    ).execute()

    data = {
        'videoId': search_response['items'][0]['id']['videoId'],
        'videoTitle': search_response['items'][0]['snippet']['title']
    }

    return data