from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from models.database import SessionLocal
from models.db_service import DBService

app = FastAPI()
db_service = DBService()
db_session = SessionLocal()


class Product(BaseModel):
    name: str
    categories_ids: Union[list, None] = None


class Category(BaseModel):
    name: str
    products_ids: Union[list, None] = None


class CategoryAdding(BaseModel):
    ids: list


class ProductAdding(BaseModel):
    ids: list


@app.get('/product/{product_id}')
def get_product(product_id: int):
    product = db_service.get_product(product_id, db_session)
    if not product:
        return {'data': 'not found product'}

    return {
                'id': product.id,
                'name': product.name,
                'categories': product.categories
            }


@app.get('/category/{category_id}')
def get_category(category_id: int):
    category = db_service.get_category(category_id, db_session)
    if not category:
        return {'data': 'not found category'}

    return {
                'id': category.id,
                'name': category.name,
                'products': category.products
            }


@app.get('/products')
def get_products():
    products = db_service.get_all_products(db_session)
    if not products:
        return {'data': 'not found products'}

    products = [
        {
            'id': product.id,
            'name': product.name,
            'categories': product.categories,
        } for product in products
    ]
    return products


@app.get('/categories')
def get_categories():
    categories = db_service.get_all_categories(db_session)
    if not categories:
        return {'data': 'not found categories'}

    categories = [
        {
            'id': category.id,
            'name': category.name,
            'products': category.products,
        } for category in categories
    ]
    return categories


@app.get('/couples')
def get_all_couples():
    couples = db_service.get_all_couples(db_session)
    if not couples:
        return {'data': 'not found couples'}

    couples = [
        {
            'product': couple[0],
            'category': couple[1],
        } for couple in couples
    ]
    return couples
