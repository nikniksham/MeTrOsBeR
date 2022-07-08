import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Couis(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'couis'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    count = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("product.id"))
    product = orm.relation('Product')

    def __repr__(self):
        return f'<Couis> Результат {self.fullname}'
