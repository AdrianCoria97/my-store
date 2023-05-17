from datetime import datetime
from domain import Seller
from domain import Buyer


class Article:
    id = str
    name: str
    item_id: int
    description: str
    category: str
    price: float
    stock: int
    seller: Seller
    buyer: Buyer
    date_created: datetime

    def __init__(self, id: str, name:str, item_id: int, description: str, category: str, price: float, stock: int,
                 seller: Seller, buyer: Buyer, date_created: datetime):
        self.id = id
        self.name = name
        self.item_id = item_id
        self.description = description
        self.category = category
        self.price = price
        self.stock = stock
        self.seller = seller
        self.buyer = buyer
        self.date_created = date_created

    # GETTERS
    def get_name_article(self):
        return self.name

    def get_item_id(self):
        return self.item_id

    def get_description(self):
        return self.description

    def get_category(self):
        return self.category

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def get_seller(self):
        return self.seller

    def get_buyer(self):
        return self.buyer

    def get_data_created(self):
        return self.date_created

    # SETTERS
    def set_name_article(self, new_name_article):
        self.name = new_name_article

    def set_item_id(self, new_item_id):
        self.item_id = new_item_id

    def set_description(self, new_description):
        self.description = new_description

    def set_category(self, new_category):
        self.category = new_category

    def set_price(self, new_price):
        self.price = new_price

    def set_stock(self, new_stock):
        self.stock = new_stock

    def set_seller(self, new_seller):
        self.seller = new_seller

    def set_buyer(self, new_buyer):
        self.buyer = new_buyer

    def set_date_created(self, new_date_created):
        self.date_created = new_date_created
