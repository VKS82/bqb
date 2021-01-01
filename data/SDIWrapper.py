import urllib.request


class SDIWrapper:

    def __init__(self, api_key, season, week):

        self._ak = api_key
        self._base_url = 'https://api.sportsdata.io/v3/nfl/'
        self.season = season
        self.week = week

    def get_games_in_progress(self):

        gip_url = 'scores/json/AreAnyGamesInProgress?key=<key>'
        contents = urllib.request.urlopen(self._base_url + gip_url.replace('<key>', self._ak, 1))
        return contents.getcode(), contents.read()


    def get_player_game_stats(self, player_id):


        gpg_url = self._base_url+'stats/json/PlayerGameStatsByPlayerID/<season>/<week>/<playerid>?key=<key>'
        gpg_url = gpg_url.replace('<season>', self.season, 1)
        gpg_url = gpg_url.replace('<week>', self.week, 1)
        gpg_url = gpg_url.replace('<key>', self._ak, 1)
        gpg_url = gpg_url.replace('<playerid>', player_id, 1)
        contents = urllib.request.urlopen(gpg_url)

        return contents.getcode(), contents.read()



if __name__ == '__main__':
    from config import SDI_KEY

    GetStats = SDIWrapper(api_key=SDI_KEY, season='2020REG', week='16')
    print(GetStats.get_games_in_progress())
    print(GetStats.get_player_game_stats(player_id='21677'))