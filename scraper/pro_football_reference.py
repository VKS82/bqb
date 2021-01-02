import pandas as pd
import yaml
import pathlib
from navigator.pfr_browser import get_pfr_page


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def load_config(ply_yaml='parameters.yaml'):
    yml = pathlib.Path.cwd() /'..'/ ply_yaml
    params = yaml.safe_load(yml.open())
    players = dict.fromkeys(params['QBS'])
    return players, params


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


def get_week(df, week):

    df = df.loc[df['General','Week'] == str(week)]
    df.columns = df.columns.droplevel()
    return df

if __name__ == "__main__":
    qbs, par = load_config()
    # for k in qbs.keys():
    #     qbs[k] = get_pfr_page(k)
    # print(qbs)


    # cn = get_stats(pfr_url='https://www.pro-football-reference.com/players/N/NewtCa00/gamelog/2020/')
    # print(cn)


    # from bqtest.pfr_dict import pfr_dict
    #
    # df = get_stats(pfr_dict['Cam Newton'])
    # df = get_week(df, week=12)
    # print(df)


