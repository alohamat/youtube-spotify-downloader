# A script which downloads music from Spotify and video/music from Youtube.

from spotdl.download.downloader import Downloader
from spotdl.utils.search import get_search_results
import yt_dlp
import asyncio # for async operations
import os # file management

def main():
    print("Welcome to Spotify and YouTube downloader!")
    while True:
        try:
            r = int(input("\nPlease select and option\n1 - Spotify\n 2 - YouTube\n0 - Exit"))
        except ValueError:
            print("Please enter a number (1-3)")
        else:
            match r:
                case 1:
                    spotify()
                case 2:
                    youtube()
                case 0:
                    print("Thanks for using my program!")
                    os.abort()
                case _:
                    print("Please select a valid option (1-3)")    

def spotify():
    pass
def youtube():
    pass

def downloadSpotify(url, directory):
    pass

def downloadYoutube(url, directory):
    pass

def change_directory():
    pass