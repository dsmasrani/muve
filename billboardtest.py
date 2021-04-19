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
playlists = sp.playlist(playlist_id='4Hbq8z7KWYVJtQQDVmN0Kf?si=HHr40zMuS7WTyJu6HoQ-fw', fields=None)
songs = list()
artists = list()
dates = list()
for i in range(len(playlists['tracks']['items'])):
    if ' (' in playlists['tracks']['items'][i]['track']['name']:
        idx = playlists['tracks']['items'][i]['track']['name'].index(' (')
        songs.append(playlists['tracks']['items'][i]['track']['name'][:idx])
    else:
        songs.append(playlists['tracks']['items'][i]['track']['name'])
    artists.append(playlists['tracks']['items'][i]['track']['artists'][0]['name'])
    dates.append(playlists['tracks']['items'][i]['added_at'][:7])
print(songs)
print(artists)
print(dates)
newdate = list()
bill = {}
for i in range(len(songs)):
    if dates[i] not in bill.keys():
        bill[dates[i]] = billboard.ChartData('hot-100',date=dates[i]+'-01',fetch=True,timeout=25)
billsongs = list()
billartist = list()
count = 0
count2 = 0
count3 = 0
for i in range(len(songs)):
    for j in range(100):
        billsongs.append(bill[dates[i]][j].title.lower())
        billartist.append(bill[dates[i]][j].artist.lower())
    #print(songs[i] + billsongs[i])
    #print(artists[i] + billartist[i])
    #if songs[i].lower() == billsongs[i].lower() and artists[i].lower() == billartist[i].lower():
        #count += 1
for i in range(len(songs)):
    if songs[i].lower() in billsongs and artists[i].lower() in billartist:
        print(songs[i])
        print(artists[i])
        count += 1
    if songs[i].lower() in billsongs:
        count2 += 1
    if artists[i].lower() in billartist:
        count3 += 1
print(songs)
print(billsongs)
print(count)
print(count2)
print(count3)
print(len(songs))
#total = len(songs)
#print(total)
#print(count/total)
#print(playlists['tracks']['items'][1]['added_at'][:10])

#def main():
    #chart = billboard.ChartData('hot-100')
    #chart1 = billboard.ChartData('hot-100',date='2015-05-22',fetch=True, timeout=25)
    #chart.title
    #song = chart[0]  # Get no. 1 song on chart
    #print(chart1)

#if __name__ == '__main__':
       #main()