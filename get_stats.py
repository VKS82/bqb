import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

row = ['Date',
       'Week',
       'Tm',
       '@',
       'Opp',
       'Result',
       'GS',
       'Cmp',
       'Att',
       'Cmp%',
       'PYards',
       'PTD',
       'Int',
       'Rate',
       'Sacks',
       ' Y_A',
       'AY_A',
       'R_Att',
       'RYards',
       'R_Y_A',
       'R_TD',
       'R_TD2',
       'Fmb',
       'FL',
       'FR',
       'FR_Yds',
       'OSnaps',
       'OSnap_Per',
       'DSnaps',
       'DSnaps_Per',
       'STSnaps',
       'STSnaps_Per']

url = 'https://www.pro-football-reference.com/players/H/HerbJu00.htm'

x = pd.read_html(url, attrs= {'id': 'stats'}, skiprows=1)

qb_stats = x[0].drop(x[0].iloc[:,35:104], axis=1)

print(qb_stats)
