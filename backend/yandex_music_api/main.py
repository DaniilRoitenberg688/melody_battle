import requests
from dulwich.cli import commands
from yandex_music import Client

import pprint

client = Client('y0__xCzoIXBBRje-AYgiaff0xJwhAZ4ws8q4msdbAt1YNOCH_CsrA').init()
# https://music.yandex.ru/users/daniilroitenberg/playlists/3?utm_source=web&utm_medium=copy_link
# command = 'https://music.yandex.ru/users/sheshelev2008/playlists/1007?utm_medium=copy_link'
# idu = command.split("/")[-3]
# album = (client.users_playlists(kind=command.split("/")[-1], user_id=idu))
# album = album.tracks
# alubmid = [x.id for x in album]
# album = (client.tracks(alubmid))
# track = album[0]
# print(album
#       )
# # import json
# # with open('a.json', 'w') as file:
# #     d = json.dumps(str(track))
# #     file.write(d)
#
# a = requests.get(track.get_cover_url())
# print(track.get_cover_url())
# with open('b.png', 'wb') as file:
#     file.write(a.content)
command = 'https://music.yandex.ru/artist/22640025?utm_source=web&utm_medium=copy_link'
ida = command.split("/")[-1]
artist = client.artists('5313769')
artist = artist[0]
print(artist.likes_count)
t = artist.get_albums()
print(sum([i.likes_count for i in t]))

# albums = (artist.get_albums())
# albumList = [await YCLIENT.albums_with_tracks(album.id) for album in albums]
# volumes = []
# for x in albumList:
#     volumes = volumes + x.volumes[0]
# track = volumes[0]
