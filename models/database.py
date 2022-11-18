from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///models/sql_app.db"

db_engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


Base = declarative_base()


association_table = Table(
    'product_category',
    Base.metadata,
    Column('product_id', ForeignKey('product.id'), primary_key=True),
    Column('category_id', ForeignKey('category.id'), primary_key=True)
)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    categories = relationship('Category', secondary=association_table, back_populates='products')

    def __repr__(self):
        return f'{self.name}'


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    products = relationship('Product', secondary=association_table, back_populates='categories')

    def __repr__(self):
        return f'{self.name}'
