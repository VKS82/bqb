from sportsreference.nfl.roster import Player
from sportsreference.nfl.roster import Roster
from sportsreference.nfl.boxscore import Boxscores
from sportsreference.nfl.boxscore import BoxscorePlayer
from sportsreference.nfl.roster import PLAYER_URL
import pandas as pd


# Deprecated PFR scraper

# saints = Roster('NOR', slim=True)
# for player in saints.players:
#     # Prints the name of all players who played for the New Orleans Saints
#     # in the most recent season.
#     print(player)

# week16 = Boxscores(16, 2020)
# print(week16.games)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

Brees_stats = BoxscorePlayer(player_id='BreeDr01', player_name='Drew Brees', player_data='<tr ><th scope="row" class="left " api-append-csv="BreeDr00" api-stat="player" ><a href="/players/B/BreeDr00.htm">Drew Brees</a></th><td class="left " api-stat="team" >NOR</td><td class="right " api-stat="pass_cmp" >19</td><td class="right " api-stat="pass_att" >26</td><td class="right " api-stat="pass_yds" >311</td><td class="right iz" api-stat="pass_td" >0</td><td class="right " api-stat="pass_int" >2</td><td class="right iz" api-stat="pass_sacked" >0</td><td class="right iz" api-stat="pass_sacked_yds" >0</td><td class="right " api-stat="pass_long" >44</td><td class="right " api-stat="pass_rating" >80.8</td><td class="right " api-stat="rush_att" >3</td><td class="right " api-stat="rush_yds" >-3</td><td class="right iz" api-stat="rush_td" >0</td><td class="right " api-stat="rush_long" >-1</td><td class="right iz" api-stat="targets" >0</td><td class="right iz" api-stat="rec" >0</td><td class="right iz" api-stat="rec_yds" >0</td><td class="right iz" api-stat="rec_td" >0</td><td class="right iz" api-stat="rec_long" >0</td><td class="right iz" api-stat="fumbles" >0</td><td class="right iz" api-stat="fumbles_lost" >0</td></tr>')
print(Brees_stats.dataframe)