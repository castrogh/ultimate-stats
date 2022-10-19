import requests
from bs4 import BeautifulSoup

res = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'html.parser')

print(soup)