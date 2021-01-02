from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pathlib import PureWindowsPath


def get_pfr_page(player_name):
    """
    Get Pro Football Reference Page for a player
    :param player_name :type str 'FirstName LastName' of a player
    :return: link :type str link to player's PFR page
    """
    link = None
    chrome_driver = PureWindowsPath('C:/Projects/bqb/navigator/chromedriver.exe')
    co = Options()
    co.add_argument("--headless")
    co.add_argument("--window-size=1920x1080")

    browser = webdriver.Chrome(options=co, executable_path=chrome_driver)

    browser.get('https://www.pro-football-reference.com/')

    elem = browser.find_element_by_name('search')
    elem.send_keys(player_name + Keys.RETURN)

    elem = browser.find_element_by_link_text(player_name)

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