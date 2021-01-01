import urllib.request
from load_players import load_players_file, filter_players


class SDIWrapper:

    def __init__(self, api_key, season, week):
        """
        Wrapper for sportsdata.io NFL API
        :param api_key: :type str,  API Key to access sportsdata.io
        :param season: :type str, <YYYY><SEASON_STAGE> e.g. '2020REG', '2020PRE', '2020POST'
        :param week: :type str, string integer 1-17 for regular season weeks, 1-4 for Post Season Weeks
        """

        self._ak = api_key
        self._base_url = 'https://api.sportsdata.io/v3/nfl/'
        self.season = season
        self.week = week
        self._player_dict = filter_players(load_players_file(), position='QB')

    def get_games_in_progress(self):
        """
        Get Games in Progress
        :return: status, response :type str 'true' or 'false'
        """
        gip_url = 'scores/json/AreAnyGamesInProgress?key=<key>'
        contents = urllib.request.urlopen(self._base_url + gip_url.replace('<key>', self._ak, 1))
        return contents.getcode(), contents.read().decode("utf-8")


    def _get_player_game_stats(self, player_id):
        """
        Get a players game stats via player ID
        :param player_id: :type str, sportsdata.io PlayerID e.g. '21677' for Tua Tagovailoa
        :return: status, response in bytes
        """

        gpg_url = self._base_url+'stats/json/PlayerGameStatsByPlayerID/<season>/<week>/<playerid>?key=<key>'
        gpg_url = gpg_url.replace('<season>', self.season, 1)
        gpg_url = gpg_url.replace('<week>', self.week, 1)
        gpg_url = gpg_url.replace('<key>', self._ak, 1)
        gpg_url = gpg_url.replace('<playerid>', player_id, 1)
        contents = urllib.request.urlopen(gpg_url)

        return contents.getcode(), contents.read()

    def get_player_stats_name(self, player_name):
        """
        Get a player game stats via player_name
        :param player_name:  :type str 'FirstName LastName'
        :return: http_status, decoded http data
        """
        status, data = self._get_player_game_stats(player_id=self._player_dict[player_name]['PlayerID'])
        return status, data.decode("utf-8")


if __name__ == '__main__':
    import coloredlogs, logging
    from config import SDI_KEY

    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger)
    GetStats = SDIWrapper(api_key=SDI_KEY, season='2020REG', week='16')
    logger.info(GetStats.get_games_in_progress())
    logger.info(GetStats.get_player_stats_name(player_name='Lamar Jackson'))