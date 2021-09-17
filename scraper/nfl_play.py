import requests
from bs4 import BeautifulSoup

test_url = 'https://www.nfl.com/games/dolphins-at-bills-2020-reg-17'

r = requests.get(test_url)
data = r.content

soup = BeautifulSoup(data, "html5lib")
print(soup.find_all(text='INT'))
