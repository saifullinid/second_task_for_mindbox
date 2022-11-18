from fastapi import FastAPI

from models.db_service import DBService

app = FastAPI()
db_service = DBService()


@app.get('/product/{product_id}')
def get_product(product_id: int):
    product = db_service.get_product(product_id)
    return {
                'id': product.id,
                'name': product.name,
                'categories': product.categories
            }


@app.get('/category/{category_id}')
def get_category(category_id: int):
    category = db_service.get_category(category_id)
    return {
                'id': category.id,
                'name': category.name,
                'products': category.products
            }


@app.get('/products')
def get_products():
    products = db_service.get_all_products()
    products = [
        {
            'id': product.id,
            'name': product.name,
            'categories': product.categories,
        } for product in products]
    return products


@app.get('/categories')
def get_categories():
    categories = db_service.get_all_categories()
    categories = [
        {
            'id': category.id,
            'name': category.name,
            'products': category.products,
        } for category in categories]
    return categories


@app.get('/couples')
def get_all_couples():
    couples = db_service.get_all_couples()
    print(couples)
    couples = [
        {
            'product': couple[0],
            'category': couple[1],
        } for couple in couples]
    return couples


@app.post('/product')
def add_product(product_name: str, categories_ids: list = None):
    product = db_service.add_product(product_name, categories_ids)
    return {
                'id': product.id,
                'name': product.name,
                'categories': product.categories,
            }


@app.post('/category')
def add_category(category_name: str, products_ids: list = None):
    category = db_service.add_category(category_name, products_ids)
    return {
                'id': category.id,
                'name': category.name,
                'products': category.products,
            }


@app.put('/product/{product_id}')
def add_categories_to_product(product_id: int, categories_ids: list):
    product = db_service.add_categories_to_product(product_id, categories_ids)
    return {
                'id': product.id,
                'name': product.name,
                'categories': product.categories,
            }


@app.put('/category/{category_id}')
def add_products_to_category(category_id: int, products_ids: list):
    category = db_service.add_products_to_category(category_id, products_ids)
    return {
                'id': category.id,
                'name': category.name,
                'products': category.products,
            }














