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


file_name = input("Enter file name: ")

with open(file_name, "w") as f:
    f.write("\n".join(titles_list))
