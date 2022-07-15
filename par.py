from bs4 import BeautifulSoup
from data import db_session
from data.category import Category
from data.product import Product
from data.couis import Couis


all_links = []


def check_old(name):
    session = db_session.create_session()
    such = session.query(Product).filter(Product.name == name).first()
    cur_id = None
    if such:
        cur_id = such.id
        for couis in such.couis:
            session.delete(couis)
        session.delete(such)
    session.commit()
    session.close()
    return cur_id


def create_category(args):
    session = db_session.create_session()
    cat = session.query(Category).filter(Category.name == args["name"]).first()
    if not cat:
        cat = Category()
        cat.name = args["name"]
        cat.link = args["link"]
        cat.father = args["father"]
        cat.pra_father = args["pra_father"]
        session.add(cat)
        session.commit()
    cat_id = cat.id
    session.close()
    return {'success': f'Категория {args["name"]} создана', 'id': int(cat_id)}


def create_product(args):
    session = db_session.create_session()
    cat = session.query(Category).filter(Category.id == args["cat_id"]).first()
    prod = Product()
    if args["cur_id"]:
        prod.id = args["cur_id"]
    prod.name = args["name"]
    prod.link = args["link"]
    prod.max_discount = args["max_discount"]
    prod.in_stoke = args["in_stoke"]
    cat.product.append(prod)
    session.merge(cat)
    # session.add(prod)
    session.commit()
    prod_id = prod.id
    session.close()
    return {'success': f'Товар {args["name"]} создан', 'id': int(prod_id)}


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


def get_count_pages(filename):
    with open(filename, encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    uls = soup.find("ul", class_="catalog-paginate v-pagination")
    count_page = int([int(l.text) for l in uls.find_all("li") if l.text.isdigit()][-1]) if uls else 1
    return count_page


def work_with(cl, stock, cat_id):
    global soup
    for g in soup.find("div", class_="subcategory-or-type__products").find_all("div", class_=cl):
        sec_g = g.find("div", class_="base-product-dropdown base-product-item__dropdown")

        variables = []
        for li in sec_g.find("ul").find_all("li"):
            te = li.text.strip().split()
            i, num = 0, ""
            while te[i].isdigit() or "." in te[i]:
                num += te[i]
                i += 1
            # print(num, te)
            price = float(num)
            count = float(te[-2])
            variables.append([price, count])

        # print(variables)
        div = g.find("div", class_="base-product-item__content")
        d = div.find("div", class_="base-product-photo")
        h1 = d.find("div", class_="base-product-photo__content")
        a = h1.find("a")
        href = "https://online.metro-cc.ru" + a.get("href")
        alt = a.get("alt")

        cur_id = check_old(alt)

        if len(variables) == 1:
            continue
        else:
            max_discount = 1 - variables[-1][0] / variables[0][0]
            if max_discount <= 0:
                continue
        prod_id = create_product(args={"name": alt, "link": href, "max_discount": max_discount, "cur_id": cur_id, "in_stoke": stock, "cat_id": cat_id})["id"]

        for price, count in variables:
            create_couis(prod_id, {"count": count, "price": price})


def upd_db(filename, cat_id):
    global soup

    with open(filename, encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # print(soup)

    work_with("base-product-item catalog-2-level-product subcategory-or-type__products-item", True, cat_id)

    work_with("base-product-item catalog-2-level-product subcategory-or-type__products-item out-of-stock", False, cat_id)

    print("Success update")
    # return get_count_pages()


def add_links(filename, li):
    global soup

    l = len(li)

    with open(filename, encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    categorii = soup.find("div", class_="catalog-filters-categories")
    father, flag, lc, ll = "", False, None, None
    for a in categorii.find_all("a"):
        link = "https://online.metro-cc.ru" + a.get("href")
        c = a.get("href")[l+1:]
        if len(c.split("/")) == 1:
            if flag:
                create_category({"name": lc, "link": ll, "father": None, "pra_father": a.get("href").split("/")[2]})
            father = c
            flag = True
        else:
            create_category({"name": c.split("/")[1], "link": link, "father": father, "pra_father": a.get("href").split("/")[2]})
            flag = False
        ll, lc = link, c
    print("Success", li)
