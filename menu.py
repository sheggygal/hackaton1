from song import Song
from songs1 import compare_song
from display_songs import print_acceptable_songs, print_unacceptable_songs

def display_menu():
    while True:
        print("\nMain Menu")
        print("1. Compare a song to Lezginka")
        print("2. Allowed playlist")
        print("3. Forbidden playlist")
        print("4. Check more songs")
        print("5. Finish")

        choice = input("Enter your choice: ")

        if choice == '1':
            compare_song()
        elif choice == '2':
            print_acceptable_songs()
        elif choice == '3':
            print_unacceptable_songs()
        elif choice == '4':
            continue
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    display_menu()
