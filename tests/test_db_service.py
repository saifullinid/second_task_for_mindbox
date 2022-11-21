import pytest

from tests.db_test import create_db_session
from models.db_service import DBService


@pytest.fixture
def session():
    yield create_db_session()


@pytest.mark.usefixtures('session')
class TestDBService:
    def test_get_all_products(self, session):
        db_service = DBService()
        products = db_service.get_all_products(session)
        products_ids = [product.id for product in products]
        exp_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert all([from_db == exp for from_db, exp in zip(products_ids, exp_ids)])

    def test_get_all_categories(self, session):
        db_service = DBService()
        categories = db_service.get_all_categories(session)
        categories_ids = [category.id for category in categories]
        exp_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert all([from_db == exp for from_db, exp in zip(categories_ids, exp_ids)])

    def test_get_all_couples(self, session):
        db_service = DBService()
        couples = db_service.get_all_couples(session)
        exp_couples = [['product_1', 'category_1'], ['product_1', 'category_2'],
                       ['product_2', 'category_1'],
                       ['product_3', 'category_3'], ['product_3', 'category_4'],
                       ['product_4', 'category_3'],
                       ['product_5', 'category_5'], ['product_5', 'category_6'],
                       ['product_6', 'category_5'],
                       ['product_7', 'category_7'], ['product_7', 'category_8'],
                       ['product_8', 'category_7']]
        assert all([from_db[0] == exp[0] and from_db[1] == exp[1] for from_db, exp in zip(couples, exp_couples)])
