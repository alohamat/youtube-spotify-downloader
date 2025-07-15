# A script which downloads music from Spotify and video/music from Youtube.

from spotdl.utils.config import DEFAULT_CONFIG
from spotdl.download.downloader import Downloader
from spotdl.types.song import Song
from spotdl.types.playlist import Playlist
from spotdl.types.album import Album
from spotdl.utils.spotify import SpotifyClient
from dotenv import load_dotenv
import yt_dlp
import asyncio # for async operations
import os # file management

load_dotenv() # loads .env file
current_dir = os.getcwd()


print("Welcome to Spotify and YouTube downloader!")
def main():
    while True:
        try:
            r = int(input("\nPlease select an option\n1 - Spotify\n2 - YouTube\n0 - Exit\n"))
        except ValueError:
            print("Please enter a number (1-3)")
        else:
            match r:
                case 1:
                    CLIENT_ID = os.getenv("CLIENT_ID")
                    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
                    if not CLIENT_ID or not CLIENT_SECRET:
                        raise RuntimeError("You need to configure CLIENT_ID and CLIENT_SECRET on .env file.")
                    SpotifyClient.init(
                        client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        user_auth=False,
                        cache_path=None,
                        no_cache=True
                    )
                    url = input('Please input a Spotify URL, Example\nhttps://open.spotify.com/intl-pt/track/7ouMYWpwJ422jRcDASZB7P?si=6fb25e0643f44cd1\n')
                    downloadSpotify(url)
                case 2:
                    youtube()
                case 0:
                    print("\nThanks for using my program!")
                    os.abort()
                case _:
                    print("\nPlease select a valid option (1-3)")    


def youtube():
    pass

def downloadSpotify(url):
    config = DEFAULT_CONFIG.copy()
    config['output'] = current_dir
    downloader = Downloader(config)

    try:
        if "track" in url:
            song = Song.from_url(url)
            print(f"\n🎵 {song.name} - {song.artist} | 💿 {song.album_name}")
            confirm = input("Download this? (s/n): ").strip().lower()
            if confirm == 's':
                downloader.download_song(song)
            else:
                return
        elif "album" in url:
            songs = Album.from_url(url).songs
            print(f'\n🎧 Album "{songs[0].album_name}" with {len(songs)} songs.')
            confirm = input("Download? (s/n): ").strip().lower()
            if confirm == 's':
                downloader.download_multiple_songs(songs)
            else:
                return
        elif "playlist" in url:
            songs = Playlist.from_url(url).songs
            print(f"\n📜 Playlist with {len(songs)} songs.")
            confirm = input("Download? (s/n): ").strip().lower()
            if confirm == 's':
                downloader.download_multiple_songs(songs)
            else:
                return
        else:
            print("❌ Invalid or not supported URL.")

    except Exception as e:
        print(f"Error: {e}")
        return

    print("\nSuccefully downloaded! saved in ", current_dir)
    r = input("\nDownload another song? (s/n)")
    if r == 's':
        otherSong = input("Spotify URL: ")
        downloadSpotify(otherSong)
    else:
        return

def downloadYoutube(url):
    pass

def change_directory():
    pass

main()