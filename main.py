from requests import get
from bs4 import BeautifulSoup
import lxml


def get_with_url(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    accept_lang = 'ru-RU,ru;q=0.9'
    headers = {
        'Accept-Language': accept_lang,
        'Accept': accept,
        'User-Agent': user_agent,
    }

    base = 'https://prnt.sc/'
    resp = get(url, headers=headers)
    if resp.status_code == 404:
        print(404)
        return
    soup = BeautifulSoup(resp.text, 'lxml')
    print(soup)


print(get_with_url("https://online.metro-cc.ru/category/bytovaya-himiya/chistyaschie-sredstva/universalnye-chistyashchie-sredstva/domestos-hvoya-15l"))