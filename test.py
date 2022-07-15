from data import db_session
from data.category import Category
from data.product import Product
from data.couis import Couis
import openpyxl

db_session.global_init("db/tovari.sqlite")

session = db_session.create_session()

wb = openpyxl.load_workbook(filename='opt.xlsx')

sheet = wb["категории"]
sheet["A1"] = "Id"
sheet["B1"] = "Название"
sheet["C1"] = "Отец"
sheet["D1"] = "Дед"
sheet["E1"] = "Ссылка"
for ind, cat in enumerate(session.query(Category).all(), start=2):
    sheet[f'A{ind}'] = cat.id
    sheet[f'B{ind}'] = cat.name
    sheet[f'C{ind}'] = cat.father
    sheet[f'D{ind}'] = cat.pra_father
    sheet[f'E{ind}'] = cat.link

sheet = wb["товары"]
sheet["A1"] = "Id"
sheet["B1"] = "Id категории"
sheet["C1"] = "Название"
sheet["D1"] = "Максимальная скидка"
sheet["E1"] = "В наличии"
sheet["F1"] = "Ссылка"
for ind, prod in enumerate(session.query(Product).all(), start=2):
    sheet[f'A{ind}'] = prod.id
    sheet[f'B{ind}'] = prod.category_id
    sheet[f'C{ind}'] = prod.name
    sheet[f'D{ind}'] = prod.max_discount
    sheet[f'E{ind}'] = prod.in_stoke
    sheet[f'F{ind}'] = prod.link

sheet = wb["цены"]
sheet["A1"] = "Id"
sheet["B1"] = "Id товара"
sheet["C1"] = "Количество"
sheet["D1"] = "Цена"
for ind, cou in enumerate(session.query(Couis).all(), start=2):
    sheet[f'A{ind}'] = cou.id
    sheet[f'B{ind}'] = cou.product_id
    sheet[f'C{ind}'] = cou.count
    sheet[f'D{ind}'] = cou.price

wb.save("opt.xlsx")
wb.close()

session.close()
