import pandas as pd


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
    qb_stats.rename(columns={'Unnamed: 29_level_0': 'Total'}, level=0, inplace=True)
    qb_stats.rename(columns={'Yds.1': 'Sack_Loss'}, level=1, inplace=True)
    qb_stats.columns = qb_stats.columns.map('|'.join).str.strip('|')
    return qb_stats


def get_week(df, week):
    df = df.loc[df['General|Week'] == str(week)]
    return df


if __name__=='__main__':
    df = get_stats(pfr_url='https://www.pro-football-reference.com/players/N/NewtCa00.htm')
    print(df.to_string())
    week = get_week(df,week='12')
    print(week.to_string())