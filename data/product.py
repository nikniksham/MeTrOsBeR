import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'product'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    article = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    couis = orm.relation('Couis')

    def __repr__(self):
        return f'<Product> Товар {self.id}'
