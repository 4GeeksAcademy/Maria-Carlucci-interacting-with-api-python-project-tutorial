import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()


# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Inicializar biblioteca Spotipy
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

response = spotify.artist_top_tracks("4dpARuHxo51G3z768sgnrY")

canciones = []
for s in response["tracks"]:
    canciones.append({
        'name': s['name'],
        'popularity': s['popularity'],
        'duration_min': s['duration_ms'] / 60000
    })

df = pd.DataFrame(canciones)
dftop3 = df.sort_values(by="popularity", ascending=False).head(3)

plt.Figure(figsize=(10,6))
plt.scatter(x=df["popularity"],y=df["duration_min"])
plt.show();

# Analizando el grafico se puede ver que no tiene relacion la popularidad con la duracion de la cancion. Hay canciones mas cortas igual de populares