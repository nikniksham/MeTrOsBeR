import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'product'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    link = sqlalchemy.Column(sqlalchemy.String)
    max_discount = sqlalchemy.Column(sqlalchemy.Integer)
    in_stoke = sqlalchemy.Column(sqlalchemy.Boolean)

    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("category.id"))
    category = orm.relation('Category')

    couis = orm.relation('Couis')

    def __repr__(self):
        return f'<Product> Товар {self.id}'
