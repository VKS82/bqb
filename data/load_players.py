import json
import pathlib
import sys


def load_players(position=None):
    json_file = pathlib.Path.cwd() / '../data' / 'Players.json'
    players = json.load(json_file.open())

    filtered = []
    if position:
        for p in players:
            if p['Position'] == position:
                filtered.append(p)
    else:
        filtered = players

    return filtered


if __name__ == '__main__':
    p_list = load_players(position='QB')
    print(sys.getsizeof(p_list))
