import time
import datetime
import os
import re
import urllib.request
import requests
from bs4 import BeautifulSoup

r = requests.get('https://wikidocs.net')
html = r.text

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.book-subject')
for title in titles:
    print(title.text)