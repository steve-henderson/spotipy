import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodError


# Get the username from the terminal

username = sys.argv[1]

# https://open.spotify.com/user/  isaacmak30?si=983f0b3315eb49f8

# Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

#create oun spotifyObject
spotifyObject = spotipy.spotify(auth=token)
