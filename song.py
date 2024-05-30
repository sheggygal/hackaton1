import requests
import psycopg2
from fetch_spoti_token import get_token, get_auth_header
from bpm_comparator import compare_bpm  # Assuming bpm_comparator.py contains the compare_bpm function
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class Song:
    def __init__(self):
        self.token = get_token()
        self.headers = get_auth_header(self.token)

    def fetch_artist_id(self, artist_name):
        url = f"https://api.spotify.com/v1/search"
        params = {
            "q": artist_name,
            "type": "artist",
            "limit": 1
        }
        response = requests.get(url, headers=self.headers, params=params)
        data = response.json()
        if data['artists']['items']:
            artist_id = data['artists']['items'][0]['id']
            return artist_id
        else:
            raise ValueError("Artist not found")

    def fetch_song_id(self, artist_id, track_title):
        url = f"https://api.spotify.com/v1/search"
        params = {
            "q": track_title,
            "type": "track",
            "limit": 1
        }
        response = requests.get(url, headers=self.headers, params=params)
        data = response.json()
        if data['tracks']['items']:
            track_id = data['tracks']['items'][0]['id']
            return track_id
        else:
            raise ValueError("Track not found")

    def fetch_song_info(self, artist_id, track_id):
        audio_features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"
        audio_response = requests.get(audio_features_url, headers=self.headers)
        audio_features = audio_response.json()

        artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
        artist_response = requests.get(artist_url, headers=self.headers)
        artist_info = artist_response.json()

        if audio_features and artist_info:
            bpm = audio_features['tempo']
            genres = artist_info.get('genres', [])
            return bpm, genres
        else:
            raise ValueError("Track or artist information not found")

    def bpm_compare(self, bpm):
        return compare_bpm(bpm)

    def save_to_db(self, artist_name, artist_id, track_title, track_id, genres, bpm, comparison_result):
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        is_bpm_acceptable = (
                    comparison_result == "Ramzan is happy, you can listen to the track publicly. It is exactly as Lezginka")
        cur.execute("""
            INSERT INTO song (id, artist_name, artist_spotify_id, song_title, song_spotify_id, genre, bpm, is_bpm_acceptable)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (track_id, artist_name, artist_id, track_title, track_id, ", ".join(genres), bpm, is_bpm_acceptable))
        conn.commit()
        cur.close()
        conn.close()


