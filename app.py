import billboard
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, session, request, redirect, render_template
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

scope = "user-library-read"
os.environ['SPOTIPY_CLIENT_ID'] = '4ee59bcc14e443ce91bbfa177eb50c23' #Secrets found in the secrets.py folder
os.environ['SPOTIPY_CLIENT_SECRET'] = '34f6fefa1b6f4acc8ea11ee89c4df6d3'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8080/login'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

caches_folder = './.spotify_caches/' #Cache path for clearing session
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path():
    return caches_folder + session.get('uuid') #Gets path


@app.route('/')
def main():
    return render_template('home.html') #initial path
    input_playlist = '4Hbq8z7KWYVJtQQDVmN0Kf?si=HHr40zMuS7WTyJu6HoQ-fw' #ONLY USE FOR DEBUGGING

@app.route('/loading')
def optionselect():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path()) #gets token for OAuth
    if not auth_manager.get_cached_token():
        return redirect('/') #if no token, redirect back home
    return render_template('loading.html') #render options.html

@app.route('/options)')
def optionselect2():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path()) #gets token for OAuth
    if not auth_manager.get_cached_token():
        return redirect('/') #if no token, redirect back home
    return render_template('options.html')

@app.route('/results)')
def results():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path()) #gets token for OAuth
    if not auth_manager.get_cached_token():
        return redirect('/') #if no token, redirect back home
    return render_template('results.html',thing_one=main())


@app.route('/result')
def result():
    return render_template('result.html',thing_one=main(id))
def getPlaylistID():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    sp1 = spotipy.Spotify(auth_manager=auth_manager)
    user_playlist = sp1.user_playlists(user=get_user_id(),limit=1,offset=0)
#    for item in user_playlist:
#        print(item)
    playlist_Data = user_playlist['items'][0]
    playlist_ID = playlist_Data['id']
    return playlist_ID


def get_user_id():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    sp1 = spotipy.Spotify(auth_manager=auth_manager)
    return str(sp1.me()['id'])

def main(inputplaylist):
    input_playlist = '4Hbq8z7KWYVJtQQDVmN0Kf?si=HHr40zMuS7WTyJu6HoQ-fw' #ONLY USE FOR DEBUGGING
    # playlists = sp.user_playlists('spotify')
    playlists = sp.playlist(playlist_id=inputplaylist, fields=None)
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
            bill[dates[i]] = billboard.ChartData('hot-100', date=dates[i] + '-01', fetch=True, timeout=25)
    billsongs = list()
    billartist = list()
    count = 0
    for i in range(len(songs)):
        for j in range(100):
            billsongs.append(bill[dates[i]][j].title.lower())
            billartist.append(bill[dates[i]][j].artist.lower())
        # print(songs[i] + billsongs[i])
        # print(artists[i] + billartist[i])
        # if songs[i].lower() == billsongs[i].lower() and artists[i].lower() == billartist[i].lower():
        # count += 1
    for i in range(len(songs)):
        if (songs[i].lower() in billsongs):
            print(songs[i] + ' ' + artists[i] + ' ')
            print(billsongs[i] + ' ' + billartist[i] + ' ')
            count += 1
#    print(songs)
#    print(billsongs)
    print(count)
    print(len(songs))
    per = round((count/len(songs)* 100))
    print(per)
    print('You are ' + str(per) + '% basic')
    # total = len(songs)
    # print(total)
    # print(count/total)
    # print(playlists['tracks']['items'][1]['added_at'][:10])

    # def main():
    # chart = billboard.ChartData('hot-100')
    # chart1 = billboard.ChartData('hot-100',date='2015-05-22',fetch=True, timeout=25)
    # chart.title
    # song = chart[0]  # Get no. 1 song on chart
    # print(chart1)
if __name__ == '__main__':
    main(inputplaylist='4Hbq8z7KWYVJtQQDVmN0Kf?si=HHr40zMuS7WTyJu6HoQ-fw')