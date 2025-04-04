import os.path

from dulwich.client import get_transport_and_path

from app.models import Track, MelodyBattle
from yandex_music import Client
from app import db
from app import client

import requests

def load_melody_battle_image(url, name):
    request = requests.get(f'{url}')

    with open(f'../frontend/public/static/melody_battles_images/{name}.png', 'wb') as file:
        file.write(request.content)



def create_melody_battle(url):
    data = url.split('/')
    user_id = data[-3]
    kind = data[-1]
    playlist = client.users_playlists(kind=kind, user_id=user_id)
    melody_battle = MelodyBattle()
    melody_battle.name = playlist.title
    melody_battle.play_list_url = url
    db.session.add(melody_battle)
    db.session.commit()
    db.session.refresh(melody_battle)
    track = playlist.tracks[0]
    track = client.tracks([track.track_id])
    image = track[0].get_cover_url()
    melody_battle.image_url = image
    load_melody_battle_image(image, melody_battle.id)
    return melody_battle



