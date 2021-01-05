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
    player_stats = pd.concat(df_list, axis=0)
    player_stats = player_stats.set_index('Player')
    player_stats = player_stats.fillna(0)
    return player_stats


if __name__ == '__main__':
    from calculate import calculate_score
    stats = main()
    results = []
    for p in list(stats.index.values):
        results.append(calculate_score(player=p, data=stats, rules=None))

    r_df = pd.DataFrame(results)
    print(r_df.to_string())

