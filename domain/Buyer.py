
class Buyer:
    # id_buyer
    name: str
    last_name: str
    age: int
    address: str
    city: str
    state: str
    postal_code: str
    phone: str
    email: str
    payment_method: str
    purchase_history: list
    shopping_cart: list
    shipping_address: str
    subscription: bool

    def __init__(self, name: str, last_name: str, age: int, address: str, city: str, state: str,
                 postal_code: str, phone: str, email: str, payment_method: str, purchase_history: list,
                 shopping_cart: list, shipping_address: str, preferences: dict, subscription: bool):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone = phone
        self.email = email
        self.payment_method = payment_method
        self.purchase_history = purchase_history
        self.shopping_cart = shopping_cart
        self.shipping_address = shipping_address
        self.preferences = preferences
        self.subscription = subscription

