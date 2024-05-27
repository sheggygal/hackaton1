from song import Song

def main_menu():
    song = Song()
    while True:
        print("1. Compare song BPM to Lezginka")
        print("2. View database")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            artist = input("Enter the artist: ")
            title = input("Enter the song title: ")
            result = song.compare_bpm(artist, title)
            print(result)
            bpm = song.fetch_song_info(artist, title)['bpm']
            song.save_to_database(artist, title, bpm, result)
        elif choice == '2':
            song.cur.execute("SELECT * FROM Songbase")
            rows = song.cur.fetchall()
            for row in rows:
                print(row)
        elif choice == '3':
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main_menu()
