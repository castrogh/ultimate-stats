import requests

res = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
res.encoding = "utf-8"

print(res)