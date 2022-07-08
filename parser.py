from bs4 import BeautifulSoup
from data import db_session
from data.product import Product
from data.couis import Couis


def create_product(args):
    session = db_session.create_session()
    such = session.query(Product).filter(Product.name == args["name"]).first()
    if not such:
        prod = Product()
        prod.name = args["name"]
        prod.link = args["link"]
        session.add(prod)
        session.commit()
        prod_id = prod.id
        session.close()
        return {'success': f'Товар {args["name"]} создан', 'id': int(prod_id)}
    session.close()
    return {"error": "Exist"}


def create_couis(prod_id, args):
    session = db_session.create_session()
    new_couis = Couis()
    new_couis.count = args["count"]
    new_couis.price = args["price"]
    prod = session.query(Product).get(prod_id)
    prod.couis.append(new_couis)
    session.merge(prod)
    # session.add(new_couis)
    session.commit()
    couis_id = new_couis.id
    session.close()
    return {'success': f'Информация добавлена', 'id': int(couis_id)}


with open("stran/test.html", encoding='utf-8') as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")

db_session.global_init("db/tovari.sqlite")

# for h1 in soup.find_all("div", class_="base-product-photo__content"):
#     a = h1.find("a")
#     href = a.get("href")
#     alt = a.get("alt")
#     # print(h1)
#     # print(a)
#     # print(href, alt)
#     # print()
#     create_product(args={"name": alt, "link": href})  # base-product-item__content

# https://online.metro-cc.ru
for g in soup.find_all("div", class_="base-product-item catalog-2-level-product subcategory-or-type__products-item"):
    div = g.find("div", class_="base-product-item__content")
    d = div.find("div", class_="base-product-photo")
    # print(d)
    h1 = d.find("div", class_="base-product-photo__content")
    a = h1.find("a")
    href = "https://online.metro-cc.ru" + a.get("href")
    alt = a.get("alt")
    # print(h1)
    # print(a)
    # print(href, alt)
    res = create_product(args={"name": alt, "link": href})
    if "error" in res:
        continue
    prod_id = res["id"]
    sec_g = g.find("div", class_="base-product-dropdown base-product-item__dropdown")
    for li in sec_g.find("ul").find_all("li"):
        # print(li.find("div").find("button").find("p").find("span").find("span").find("span").text, li.text)
        te = li.text.split()
        price = te[0]
        count = te[-2]
        # print(te)
        create_couis(prod_id, {"count": count, "price": price})
        # print(price, count)
    # print()
    # create_product(args={"name": alt, "link": href})