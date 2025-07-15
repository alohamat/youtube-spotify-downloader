# A script which downloads music from Spotify and video/music from Youtube.

from spotdl.utils.config import DEFAULT_CONFIG
from spotdl.download.downloader import Downloader
from spotdl.utils.search import get_search_results
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
            r = int(input("\nPlease select an option\n1 - Spotify\n2 - YouTube\n0 - Exit"))
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
                    url = input('Please input a Spotify URL IN QUOTES, Example\n"https://open.spotify.com/intl-pt/track/7ouMYWpwJ422jRcDASZB7P?si=6fb25e0643f44cd1"\n')
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

    search_results = get_search_results(url)
    if not search_results:
        print("\nNothing found, please try again.")
        main()
    
    song = search_results[0]    
    result = downloader.download_song(song)
    print("\nSuccefully downloaded! saved in ", current_dir)
    r = input("\nDownload another song? (s/n)")
    if r == 's':
        otherSong = input("Spotify URL: ")
        downloadSpotify(otherSong)
    else:
        main()

def downloadYoutube(url):
    pass

def change_directory():
    pass

main()