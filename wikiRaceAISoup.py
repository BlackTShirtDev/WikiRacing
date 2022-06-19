#import wordnet as wn

#Regular expressions lib
import re

from bs4 import BeautifulSoup
import html5lib
import urllib3

webUrl = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
total_added = 0


def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data, "html5lib")


soup = make_soup(webUrl)
results = soup.find_all('a', {'href': re.compile(r'/wiki/')})

for result in results:

    print(result.attrs)




