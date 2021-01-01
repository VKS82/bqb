import json
import pathlib
import sys


def load_players_file():
    json_file = pathlib.Path.cwd() / '../data' / 'Players.json'
    players = json.load(json_file.open())

    p_dict = {}
    for p in players:
        name = p['FirstName'] + ' ' +p['LastName']

        p_dict[name] ={'PlayerID': str(p['PlayerID']), 'Team': p['Team'], 'Position': p['Position']}
    return p_dict


def filter_players(player_dict, position):
    nd = player_dict.copy()
    for k in player_dict.keys():
        if player_dict[k]['Position'] != position:
            del nd[k]

    return nd


if __name__ == '__main__':
    p_dict = load_players()
    p_dict = filter_players(player_dict=p_dict, position='QB')
    print(sys.getsizeof(p_dict))
    print(len(p_dict))
    print(p_dict)
