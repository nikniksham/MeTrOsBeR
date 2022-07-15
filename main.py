from data import db_session
from download_page import download

# link = ["https://online.metro-cc.ru/category/ovoshchi-i-frukty/ovoshchi", "https://online.metro-cc.ru/category/alkogolnaya-produkciya/krepkiy-alkogol/viski"]
link = ['https://online.metro-cc.ru/category/alkogolnaya-produkciya', 'https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca', 'https://online.metro-cc.ru/category/bakaleya', 'https://online.metro-cc.ru/category/myasnye', 'https://online.metro-cc.ru/category/myasnaya-gastronomiya', 'https://online.metro-cc.ru/category/rybnye', 'https://online.metro-cc.ru/category/ovoshchi-i-frukty', 'https://online.metro-cc.ru/category/chaj-kofe-kakao', 'https://online.metro-cc.ru/category/hleb-vypechka-konditerskie-izdeliya', 'https://online.metro-cc.ru/category/bezalkogolnye-napitki', 'https://online.metro-cc.ru/category/zdorovoe-pitanie', 'https://online.metro-cc.ru/category/gotovye-bljuda-polufabrikaty', 'https://online.metro-cc.ru/category/tovary-dlya-doma-dachi-sada', 'https://online.metro-cc.ru/category/bytovaya-himiya', 'https://online.metro-cc.ru/category/kosmetika', 'https://online.metro-cc.ru/category/avtotovary', 'https://online.metro-cc.ru/category/elektronika-tekhnika', 'https://online.metro-cc.ru/category/tovary-dlja-zhivotnyh', 'https://online.metro-cc.ru/category/detskie-tovary', 'https://online.metro-cc.ru/category/professionalnoe-oborudovanie', 'https://online.metro-cc.ru/category/vse-dlya-remonta', 'https://online.metro-cc.ru/category/ofis-obuchenie-hobbi', 'https://online.metro-cc.ru/category/antibakterialnaya-produkciya']
# https://online.metro-cc.ru/category/alkogolnaya-produkciya/krepkiy-alkogol/viski

db_session.global_init("db/tovari.sqlite")

download()
