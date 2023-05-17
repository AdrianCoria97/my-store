from typing import List
from domain.Article import Article
from domain.Seller import Seller


class Store:
    id: str
    store_name: str
    products: List[Article]
    employees: List[Seller]
    sales_of_the_month: int

    def __init__(self, id: str, store_name: str, products: List[Article], employees: List[Seller],
                 sales_of_the_month: int):
        self.id = id
        self.store_name = store_name
        self.products = products
        self.employees = employees
        self.sales_of_the_month = sales_of_the_month

    # GETTERS
    def get_store(self):
        return self.store_name

    def get_products(self):
        return self.products

    def get_employees(self):
        return self.employees

    def get_sales_of_the_month(self):
        return self.sales_of_the_month

    # SETTERS
    def set_store_name(self, new_store_name):
        self.store_name = new_store_name

    def set_products(self, new_products):
        self.products = new_products

    def set_employees(self, new_employees):
        self.employees = new_employees

    def set_sales_of_the_month(self, new_sales_of_the_month):
        self.sales_of_the_month = new_sales_of_the_month
