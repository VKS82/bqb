import pandas as pd
import yaml
import pathlib

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def load_players(ply_yaml='parameters.yaml'):
    yml = pathlib.Path.cwd() / ply_yaml
    player_dict = yaml.safe_load(yml.open())
    return dict.fromkeys(player_dict['QBS'])


def get_pfr_url(ply_dict):

    return False


def get_stats(pfr_url):

    qb_stats = pd.read_html(pfr_url, attrs= {'id': 'stats'}, skiprows=0)

    qb_stats = qb_stats[0].drop(qb_stats[0].iloc[:, 35:104], axis=1)

    qb_stats.rename(columns={'Unnamed: 0_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 1_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 2_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 3_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 4_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 5_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 6_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 22_level_0': 'Rush_TD_2'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 3_level_1': 'Home_Road'},level=1, inplace=True)

    return qb_stats


if __name__ == "__main__":
    qbs = load_players()
    print(qbs)

    test_url =  'https://www.pro-football-reference.com/players/H/HerbJu00.htm'