"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
titles = soup.select('a[data-tpl="l"] p.indicate-hover')

titles_list = []
for t in titles:
    titles_list.append(t.text.strip())

print(*titles_list, sep="\n")
