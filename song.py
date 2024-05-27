import psycopg2
import requests


class Song:
    def __init__(self):
        # Initialize database connection
        self.conn = psycopg2.connect(database="ramzan", user="postgres", password="Ekeva12", host="localhost",
                                     port="5432")
        self.cur = self.conn.cursor()

    def fetch_song_info(self, artist, title):
        # Fetch song information from Spotify API
        url = "https://api.spotify.com/v1/search"
        params = {
            'q': f'artist:{artist} track:{title}',
            'type': 'track'
        }
        headers = {
            'Authorization': 'Bearer YOUR_SPOTIFY_ACCESS_TOKEN'
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if 'tracks' in data and 'items' in data['tracks'] and data['tracks']['items']:
            track_info = data['tracks']['items'][0]
            return {
                'artist': track_info['artists'][0]['name'],
                'title': track_info['name'],
                'bpm': 120
            }
        else:
            return None

    def compare_bpm(self, artist, title):
        # Compare BPM to 80 and 110
        song_info = self.fetch_song_info(artist, title)
        if not song_info:
            return "Song not found"

        bpm = song_info['bpm']
        if 80 <= bpm <= 110:
            return "Ramzan is happy, you can listen to the track publicly. It is exactly as Lezginka"
        else:
            return "Either ravers, or doom-metalists are prohibited in Chechnya. Don't go there."

    def save_to_database(self, artist, title, bpm, result):
        # Save song information to the database
        self.cur.execute("INSERT INTO Songbase (artist, title, bpm, result) VALUES (%s, %s, %s, %s)",
                         (artist, title, bpm, result))
        self.conn.commit()
