import pytest
import requests


class TestAPI:
    '''
    Запуск тестов производим при запущенном сервере:
        uvicorn main:app
    '''

    def test_get_products(self):
        '''
        Проверяем:
            status_code
            наличие ключа 'categories' во всех полученных <product>
            наличие пустых словарей 'categories' хотя бы в одном <product>
        '''

        response = requests.get('http://127.0.0.1:8000/products')

        empty_categories_in_product_found = False

        for product_dict in response.json():
            if len(product_dict.get('categories')) == 0:
                empty_categories_in_product_found = True

        assert response.status_code == 200
        assert all('categories' in product_dict for product_dict in response.json())
        assert empty_categories_in_product_found

    def test_get_categories(self):
        '''
        Проверяем:
            status_code
            наличие ключа 'products' во всех полученных <category>
            наличие пустых словарей 'products' хотя бы в одной <category>
        '''

        response = requests.get('http://127.0.0.1:8000/categories')

        empty_products_in_category_found = False

        for category_dict in response.json():
            if len(category_dict.get('products')) == 0:
                empty_products_in_category_found = True

        assert response.status_code == 200
        assert all('products' in category_dict for category_dict in response.json())
        assert empty_products_in_category_found

    def test_get_couples(self):
        '''
        Проверяем:
            status_code
            наличие ключей 'product' и 'category' во всех полученных <couple>
            отсутствие пустых значений по ключам 'product' и 'category' во всех <couple>
        '''

        response = requests.get('http://127.0.0.1:8000/couples')

        print(response.json())

        assert response.status_code == 200
        assert all('product' in couple_dict and 'category' in couple_dict
                   for couple_dict in response.json())
        assert all(couple_dict.get('product') and couple_dict.get('category')
                   for couple_dict in response.json())
