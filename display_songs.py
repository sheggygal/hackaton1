import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def print_acceptable_songs():
    conn = get_connection()
    if not conn:
        return

    try:
        cur = conn.cursor()

        # Query to select songs with acceptable BPM
        cur.execute("""
            SELECT artist_name, song_title, bpm, genre 
            FROM song 
            WHERE is_bpm_acceptable = TRUE;
        """)
        acceptable_songs = cur.fetchall()

        print("Songs with acceptable BPM:")
        for song in acceptable_songs:
            artist_name, song_title, bpm, genre = song
            print(f"Artist: {artist_name}, Title: {song_title}, BPM: {bpm}, Genre: {genre}")
            print("Ramzan is happy, you can listen to that playlist publicly. It is exactly as Lezginka.\n")

        cur.close()
    except Exception as e:
        print(f"Error retrieving data from the database: {e}")
    finally:
        conn.close()

def print_unacceptable_songs():
    conn = get_connection()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute("""
            SELECT artist_name, song_title, bpm, genre 
            FROM song 
            WHERE is_bpm_acceptable = FALSE;
        """)
        unacceptable_songs = cur.fetchall()

        print("Songs with unacceptable BPM:")
        for song in unacceptable_songs:
            artist_name, song_title, bpm, genre = song
            print(f"Artist: {artist_name}, Title: {song_title}, BPM: {bpm}, Genre: {genre}")
            print("Never listen to this in Chechnya. YOU MUST BE SORRY!\n")

        cur.close()
    except Exception as e:
        print(f"Error retrieving data from the database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print_acceptable_songs()
    print_unacceptable_songs()
