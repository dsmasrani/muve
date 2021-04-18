import billboard
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"
os.environ['SPOTIPY_CLIENT_ID'] = '4ee59bcc14e443ce91bbfa177eb50c23' #Secrets found in the secrets.py folder
os.environ['SPOTIPY_CLIENT_SECRET'] = '34f6fefa1b6f4acc8ea11ee89c4df6d3'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8080/login'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

def main():
    chart = billboard.ChartData('hot-100')
    chart1 = billboard.ChartData('hot-100',date='2015-05-22',fetch=True, timeout=25)
    chart.title
    song = chart[0]  # Get no. 1 song on chart
    print(chart1)

if __name__ == '__main__':
    main()