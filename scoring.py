import yaml
import pathlib
import coloredlogs, logging
import pandas as pd
from navigator.pfr_browser import get_pfr_page
from scraper.pro_football_reference import get_stats, get_week


def load_config(ply_yaml='parameters.yaml'):
    yml = pathlib.Path.cwd() / ply_yaml
    params = yaml.safe_load(yml.open())
    players = dict.fromkeys(params['QBS'])
    return players, params


def main(loglevel='DEBUG'):
    logger = logging.getLogger(__name__)
    coloredlogs.install(level=loglevel, logger=logger)
    qbs, params = load_config()
    logger.debug('QBS : {} | Parameters : {}'.format(qbs, params))

    df_list = []
    for k in qbs.keys():
        qbs[k] = [get_pfr_page(k)]
        logger.debug('QB | URL : {}'.format(qbs[k]))
        df = get_stats(pfr_url=qbs[k][0])
        df = get_week(df, week=params['Week'])

        df['Player'] = k
        df_list.append(df)
    return df_list


if __name__ == '__main__':
    import pickle
    df_list = main()
    df_pi = open('df_list.obj', 'wb')
    pickle.dump(df_list, df_pi)
