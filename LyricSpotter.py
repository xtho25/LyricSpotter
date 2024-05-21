import spotipy
from spotipy.oauth2 import SpotifyOAuth
import syncedlyrics
import json
import tkinter as tk
import tkinter.font as font
from datetime import datetime
import time

DEBUG_MODE=True

UPDATE_WAIT_TIME=0.1

root = tk.Tk()
root.title("Lyrics finder")
root.attributes("-topmost", True)
root.overrideredirect(True)
root.configure(bg='#03020d')

get_font = font.Font(family="Arial", size="22", weight="normal")

lyrics_label = tk.Label(root, text="Starting...", bg="#03020d", fg="#dfe0eb", font=get_font)
lyrics_label.pack(expand=True)

scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='<CLIENT_ID>',
                                               client_secret='<CLIENT_SECRET>',
                                               scope=scope,
                                               redirect_uri='https://google.com/'))

lyrics=[]
s_timestamps=[]
track_name=''
artist_name=''
is_playing=False
prog_sec=0

def get_current_track():
    global track_name,is_playing,prog_ms,prog_sec,artist_name
    current_track = sp.current_user_playing_track()

    if current_track == None or (current_track['item'] == None):
        no_song_on_spotify()
        return


    artist_name = current_track['item']['artists'][0]['name']
    track_name=current_track['item']['name']
    is_playing=current_track['is_playing']
    prog_ms=current_track['progress_ms']
    prog_sec=prog_ms/1000
    
    if DEBUG_MODE: print(f'Track info gotten. {track_name}, {artist_name}')

    get_lyrics()

def get_lyrics():
    lyrics_lrc = syncedlyrics.search(f"{track_name} {artist_name}")
    if lyrics_lrc:
        lyrics_split=lyrics_lrc.split('\n')

        for line in lyrics_split:
            timestamp=line[:9]
            timestamp=timestamp[1:]
            lyric = line[11:]
            
            if lyric == '': lyric='\u266a'
            
            lyrics.append(lyric)
            time_obj = datetime.strptime(timestamp, "%M:%S.%f")
            seconds = (time_obj.minute * 60) + time_obj.second + (time_obj.microsecond / 1000000)
            s_timestamps.append(seconds)
        
        if DEBUG_MODE: print('Lyrics found and formatted.')

        display_lyrics()
    else: no_song_on_spotify()
  
def display_lyrics():
    if lyrics:
        for i in range(0, len(s_timestamps)):
            if s_timestamps[i] < prog_sec and s_timestamps[i+1] > prog_sec:
                verse=lyrics[i]
                break
            elif s_timestamps[0] > prog_sec:
                verse=lyrics[0]
                break
        
        lyrics_label.config(text=verse)
        if DEBUG_MODE: print('Config complete.')
    else: no_song_on_spotify()

def update_label():
    while True:
        try:
            get_current_track()
            time.sleep(UPDATE_WAIT_TIME)
            root.update()
        except Exception as e:
            if DEBUG_MODE: print(e)


def no_song_on_spotify():
    if DEBUG_MODE: print('No song is beeing heard on Spotify.')
    lyrics_label.config(text='No song is beeing heard on Spotify.')

if __name__ == '__main__':
    update_label()

