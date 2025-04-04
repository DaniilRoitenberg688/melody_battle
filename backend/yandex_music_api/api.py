import yandex_music
from errors import PlayListError
from pprint import pprint


def parse_playlist(client: yandex_music.Client, url: str):
    # try:
    result = []
    data = url.split('/')
    user_id = data[-3]
    kind = data[-1]
    playlist = client.users_playlists(kind=kind, user_id=user_id).tracks
    pprint(playlist)
    ids = [i.id for i in playlist]
    playlist = client.tracks(ids)
    track: yandex_music.Track
    for track in playlist:
        track_parsed = {
            'title': track.title,
            'artists': [i for i in track.artists_name()],
            'icon': track.cover_uri,

        }
        print(track.cover_uri)
        result.append(track_parsed)


# except Exception as e:
#     print(e)
#     raise PlayListError(message='something went wrong while parsing playlist')


if __name__ == '__main__':
    client = yandex_music.Client(token='y0__xCzoIXBBRje-AYgiaff0xJwhAZ4ws8q4msdbAt1YNOCH_CsrA').init()
    url = 'https://music.yandex.ru/users/daniilroitenberg/playlists/1002?utm_source=desktop&utm_medium=copy_link'
    parse_playlist(client, url)
