from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pathlib import PureWindowsPath
from selenium.common.exceptions import *

def get_pfr_page(player_name):
    """
    Get Pro Football Reference Page for a player
    :param player_name :type str 'FirstName LastName' of a player
    :return: link :type str link to player's PFR page
    """
    if player_name == 'Josh Allen':
        return 'https://www.pro-football-reference.com/players/A/AlleJo02.htm'
    if player_name == 'Trevor Lawrence':
        return 'https://www.pro-football-reference.com/players/L/LawrTr00.htm'
    if player_name == 'Justin Herbert':
        return 'https://www.pro-football-reference.com/players/H/HerbJu00.htm'
    link = None
    chrome_driver = PureWindowsPath('C:/Projects/bqb/navigator/chromedriver.exe')
    co = Options()
    co.add_argument("--headless")
    co.add_argument("--window-size=1920x1080")

    browser = webdriver.Chrome(options=co, executable_path=chrome_driver)

    browser.get('https://www.pro-football-reference.com/')

    elem = browser.find_element_by_name('search')
    elem.send_keys(player_name + Keys.RETURN)
    try:
        elem = browser.find_element_by_link_text(player_name)
    except NoSuchElementException:
        first, last = player_name.split(sep=' ')
        link = 'https://www.pro-football-reference.com/players/{}/{}{}00.htm'.format(last[0], last[0:4], first[0:2])
        return link

    link = elem.get_attribute('href')
    browser.quit()

    return link


def get_game_log_page(link, year):
    """
    :param link: PFR player link
    :param year: :type str Year in 'YYYY' format
    :return: :type str PFR gamelog link for year
    """
    gl_str = 'gamelog/<year>/'.replace('<year>', year)
    return link.replace('.htm',gl_str)


if __name__=='__main__':
    Daniel_Jones_link = get_pfr_page(player_name='Daniel Jones')
    print(Daniel_Jones_link)