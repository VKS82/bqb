import json
import pathlib
import sys


def load_players_file():
    """
    Load Players from sportsdta.io JSON
    :return: p_dict dictionary in form of
    p_dict[FirstName LastName] = {'PlayerID' : <str>, 'Team': <str>, 'Position': <str>}
    """
    json_file = pathlib.Path.cwd() / 'SDI_Players.json'
    players = json.load(json_file.open())

    p_dict = {}
    for p in players:
        name = p['FirstName'] + ' ' +p['LastName']

        p_dict[name] ={'PlayerID': str(p['PlayerID']), 'Team': p['Team'], 'Position': p['Position']}
    return p_dict


def filter_players(player_dict, position):
    """
    Filter player_dict, return a copy with records player_dict[FirstName LastName][Position] match position.
    :param player_dict: dictionary of form
    p_dict[FirstName LastName] = {'PlayerID' : <str>, 'Team': <str>, 'Position': <str>}
    :param position: str, 'QB', 'WR', 'RB', 'DL,'LB','DB'
    :return: nd, filtered dictionary with only records that match position
    """
    nd = player_dict.copy()
    for k in player_dict.keys():
        if player_dict[k]['Position'] != position:
            del nd[k]

    return nd


if __name__ == '__main__':
    p_dict = load_players_file()
    p_dict = filter_players(player_dict=p_dict, position='QB')
    print(sys.getsizeof(p_dict))
    print(len(p_dict))
    print(p_dict)
