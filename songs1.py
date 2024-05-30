from song import Song

def compare_song():
    song = Song()
    artist_name = input("Enter artist name: ")
    track_title = input("Enter track title: ")

    try:
        artist_id = song.fetch_artist_id(artist_name)
        track_id = song.fetch_song_id(artist_id, track_title)
        bpm, _ = song.fetch_song_info(artist_id, track_id)
        comparison_result = song.bpm_compare(bpm)
        print(f"Comparison Result: {comparison_result}")

        # Save song to database
        song.save_to_db(artist_name, artist_id, track_title, track_id, [], bpm, comparison_result)
        print("Song saved to the database successfully.")
    except ValueError as e:
        print(e)