import billboard
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"
os.environ['SPOTIPY_CLIENT_ID'] = '4ee59bcc14e443ce91bbfa177eb50c23' #Secrets found in the secrets.py folder
os.environ['SPOTIPY_CLIENT_SECRET'] = '34f6fefa1b6f4acc8ea11ee89c4df6d3'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8080/login'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#playlists = sp.user_playlists('spotify')
playlists = sp.playlist(playlist_id='7nZBZCS7WncuuuQv2to8Qj?si=565a56bf6b0f4ed2&nd=1', fields=None)
user_playlist = sp.user_playlists(user=get_user_id(),limit=1,offset=0)
#    for item in user_playlist:
#        print(item)
playlist_Data = user_playlist['items'][0]
playlist_ID = playlist_Data['id']
print(playlists)
def main():
    chart = billboard.ChartData('hot-100')
    chart1 = billboard.ChartData('hot-100',date='2015-05-22',fetch=True, timeout=25)
    chart.title
    song = chart[0]  # Get no. 1 song on chart
    print(chart1)

#if __name__ == '__main__':
#       main()