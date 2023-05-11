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
    average_rating: float
    comments: [str]
    date_created: datetime
    shipping_methods: [str]

    def __init__(self, id, name, item_id, description, category, price, stock, seller, buyer, average_rating, comments, date_created, shipping_methods):
        self.id = id
        self.name = name
        self.item_id = item_id
        self.description = description
        self.category = category
        self.price = price
        self.stock = stock
        self.seller = seller
        self.buyer = buyer
        self.average_rating = average_rating
        self.comments = comments
        self.date_created = date_created
        self.shipping_methods = shipping_methods
