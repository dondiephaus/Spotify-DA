from credentials import client_id, client_secret
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)
username = ""
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = "user-library-read"
token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("No token for ", username)
