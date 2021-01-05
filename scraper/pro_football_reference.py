import pandas as pd


def get_stats(pfr_url):

    qb_stats = pd.read_html(pfr_url, attrs= {'id': 'stats'}, skiprows=0)

    qb_stats = qb_stats[0]

    qb_stats.rename(columns={'Unnamed: 0_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 1_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 2_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 3_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 4_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 5_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 6_level_0': 'General'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 22_level_0': 'Total'},level=0, inplace=True)
    qb_stats.rename(columns={'Unnamed: 3_level_1': 'Home_Road'},level=1, inplace=True)
    qb_stats.rename(columns={'Unnamed: 29_level_0': 'Total'}, level=0, inplace=True)
    qb_stats.rename(columns={'Yds.1': 'Sack_Loss'}, level=1, inplace=True)
    qb_stats.columns = qb_stats.columns.map('|'.join).str.strip('|')

    rcv_cols = ['Receiving|Tgt', 'Receiving|Rec', 'Receiving|Yds', 'Receiving|Y/R',
                'Receiving|TD', 'Receiving|Ctch%', 'Receiving|Y/Tgt']

    if rcv_cols[0] not in qb_stats.columns:
        for rc in rcv_cols:
            qb_stats[rc] = 0

    return qb_stats


def get_week(df, week):
    df = df.loc[df['General|Week'] == str(week)]
    return df


if __name__=='__main__':
    df = get_stats(pfr_url='https://www.pro-football-reference.com/players/N/NewtCa00.htm')
    print(df.to_string())
    week = get_week(df,week='12')
    print(week.to_string())