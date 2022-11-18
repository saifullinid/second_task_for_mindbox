from models.database import Product, Category, association_table, SessionLocal

db_session = SessionLocal()


class DBService:
    def add_category(self, category_name, products_ids: list):
        category = Category(name=category_name)
        if products_ids:
            products = db_session.query(Product).filter(Product.id.in_(products_ids))
            category.products = [product for product in products]
        db_session.add(category)
        try:
            db_session.commit()
        except Exception as ex:
            print(ex)
        finally:
            db_session.close()
        category = db_session.query(Category).filter(Category.name == category_name).first()
        return category

    def add_product(self, product_name, categories_ids: list):
        product = Product(name=product_name)
        if categories_ids:
            categories = db_session.query(Category).filter(Category.id.in_(categories_ids))
            product.categories = [category for category in categories]
        db_session.add(product)
        try:
            db_session.commit()
        except Exception as ex:
            print(ex)
        finally:
            db_session.close()
        product = db_session.query(Product).filter(Product.name == product_name).first()
        return product

    def add_categories_to_product(self, product_id, categories_ids: list):
        product = self.get_product(product_id)
        categories = db_session.query(Category).filter(Category.id.in_(categories_ids))
        current_categories = [*product.categories, *categories]
        product.categories = [category for category in current_categories]
        db_session.add(product)
        try:
            db_session.commit()
        except Exception as ex:
            print(ex)
        finally:
            db_session.close()
        product = self.get_product(product_id)
        return product

    def add_products_to_category(self, category_id, products_ids: list):
        category = self.get_category(category_id)
        products = db_session.query(Product).filter(Product.id.in_(products_ids))
        current_products = [*category.products, *products]
        category.products = [product for product in current_products]
        db_session.add(category)
        try:
            db_session.commit()
        except Exception as ex:
            print(ex)
        finally:
            db_session.close()
        category = self.get_category(category_id)
        return category

    def get_product(self, product_id):
        return db_session.query(Product).filter(Product.id == product_id).first()

    def get_category(self, category_id):
        return db_session.query(Category).filter(Category.id == category_id).first()

    def get_all_products(self):
        return db_session.query(Product)

    def get_all_categories(self):
        return db_session.query(Category).all()

    def get_all_couples(self):
        product_category_couples = db_session\
            .query(Product.name, Category.name)\
            .select_from(
                association_table.join(Product).join(Category)
            )\
            .order_by(Product.name).all()
        return product_category_couples
