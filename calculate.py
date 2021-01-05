import pickle
import pathlib
import yaml
import pandas as pd

DF_COLS = ['General|Date', 'General|Week', 'General|Tm', 'General|Home_Road',
       'General|Opp', 'General|Result', 'General|GS', 'Passing|Cmp',
       'Passing|Att', 'Passing|Cmp%', 'Passing|Yds', 'Passing|TD',
       'Passing|Int', 'Passing|Rate', 'Passing|Sk', 'Passing|Sack_Loss',
       'Passing|Y/A', 'Passing|AY/A', 'Rushing|Rush', 'Rushing|Yds',
       'Rushing|Y/A', 'Rushing|TD', 'Receiving|Tgt', 'Receiving|Rec',
       'Receiving|Yds', 'Receiving|Y/R', 'Receiving|TD', 'Receiving|Ctch%',
       'Receiving|Y/Tgt', 'Total|TD', 'Fumbles|Fmb', 'Fumbles|FL',
       'Fumbles|FF', 'Fumbles|FR', 'Fumbles|Yds', 'Fumbles|TD',
       'Off. Snaps|Num', 'Off. Snaps|Pct', 'Def. Snaps|Num', 'Def. Snaps|Pct',
       'ST Snaps|Num', 'ST Snaps|Pct', 'Player']


def load_config(cfg_yaml='scoring_rules.yaml'):
    yml = pathlib.Path.cwd() / cfg_yaml
    params = yaml.safe_load(yml.open())
    return params



def calculate_score(player,data,rules=None):
    if not rules:
        rules = load_config()

    score = 0
    score += (int(data.at[player, 'Passing|Cmp'])*rules['Completion'][0]) // rules['Completion'][1]

    incompletions =  int(data.at[player, 'Passing|Att']) - int(data.at[player, 'Passing|Cmp'])
    score += (incompletions* rules['Incompletion'][0]) // rules['Incompletion'][1]

    score += (int(data.at[player, 'Passing|Sk'])*rules['Sack'][0]) // rules['Sack'][1]

    score += (int(data.at[player, 'Passing|TD'])*rules['Pass_TD'][0]) // rules['Pass_TD'][1]
    score += (int(data.at[player, 'Rushing|TD']) * rules['Rush_TD'][0]) // rules['Rush_TD'][1]

    score += (int(data.at[player, 'Passing|Yds']) * rules['Pass_Yards'][0]) // rules['Pass_Yards'][1]
    score += (int(data.at[player, 'Rushing|Yds']) * rules['Rush_Yards'][0]) // rules['Rush_Yards'][1]


    score += (int(data.at[player, 'Passing|Int']) * rules['Interception'][0]) // rules['Interception'][1]
    score += (int(data.at[player, 'Fumbles|Fmb']) * rules['Fumble'][0]) // rules['Fumble'][1]

    return score

if __name__ == '__main__':
    df_fh = open('df_list.obj', 'rb')
    df = pickle.load(df_fh)
    df = df.set_index('Player')
    sr = load_config()

    for p in list(df.index.values):
        result = calculate_score(player=p, data=df, rules=sr)
        print('Player : {}, BQB Score :  {}'.format(p, result))





