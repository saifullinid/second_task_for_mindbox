from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from models.database import Base, Product, Category, association_table

SQLALCHEMY_DATABASE_URL = "sqlite://"


def create_db_session():
    '''
        Создаем тестовую БД sqlite в памяти
    '''

    db_engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    db_session = session_local()
    Base.metadata.create_all(db_engine)

    filling_test_db(db_session, db_engine)

    return db_session


def filling_test_db(session, engine):
    '''
    заполняем БД данными:
        products: 'product_1' ... 'product_10'
        categories: 'category_1' ... 'category_10'
        association_table relations:
            [product_id, category_id]
            [1, 1], [1, 2],
            [2, 1],
            [3, 3], [3, 4],
            [4, 3]
            [5, 5], [5, 6],
            [6, 5],
            [7, 7], [7, 8],
            [8, 7]
    '''

    for i in range(1, 11):
        product = Product(name=f'product_{i}')
        category = Category(name=f'category_{i}')
        session.add(product)
        session.add(category)
    session.commit()
    session.close()

    with engine.connect() as conn:
        for i in [[1, 1], [1, 2], [2, 1], [3, 3], [3, 4], [4, 3],
                  [5, 5], [5, 6], [6, 5], [7, 7], [7, 8], [8, 7]]:
            ins = insert(association_table).values(product_id=i[0], category_id=i[1])
            conn.execute(ins)
