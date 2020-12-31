import urllib.request
from config import SDI_KEY



url_games_inprogress =  'https://api.sportsdata.io/v3/nfl/scores/json/AreAnyGamesInProgress?key=<key>'.replace('<key>', SDI_KEY, 1)

contents = urllib.request.urlopen(url_games_inprogress)

print(contents.getcode())

print(contents.read())