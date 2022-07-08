import requests
from bs4 import BeautifulSoup

url = 'https://online.metro-cc.ru/category/bytovaya-himiya/chistyaschie-sredstva/universalnye-chistyashchie-sredstva/domestos-hvoya-15l'
r = requests.get(url)
soup_ing = str(BeautifulSoup(r.content, 'lxml'))
soup_ing = soup_ing.encode()

with open("stran/test2.html", "wb") as file:
    file.write(soup_ing)