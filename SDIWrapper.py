import urllib.request


class SDIWrapper:

    def __init__(self, api_key='None'):

        self._ak = api_key
        self._base_url = 'https://api.sportsdata.io/v3/nfl/'

    def get_games_in_progress(self):

        gip_url = 'scores/json/AreAnyGamesInProgress?key=<key>'
        contents = urllib.request.urlopen(self._base_url + gip_url.replace('<key>', self._ak, 1))
        return contents.getcode(), contents.read()


if __name__ == '__main__':
    from config import SDI_KEY

    GetStats = SDIWrapper(api_key=SDI_KEY)
    print(GetStats.get_games_in_progress())