from domain.Client import Client


class Buyer(Client):

    purchase_history: list
    shopping_cart: list
    shipping_address: str
    has_subscribed: bool

    def __init__(self, purchase_history: list, shopping_cart: list, shipping_address: str, has_subscribed: bool,
                 id: str, name: str, last_name: str, age: int, address: str, city: str, zip_code: str,
                 phone: str, email: str, status: bool):

        # Con super llamamos a los metodos de la clase padre
        super().__init__(id, name, last_name, age, address, city, zip_code, phone, email, status)
        self.purchase_history = purchase_history
        self.shopping_cart = shopping_cart
        self.shipping_address = shipping_address
        self.has_subscribed = has_subscribed

    # GETTERS
    def get_purchase_history(self):
        return self.purchase_history

    def get_shopping_cart(self):
        return self.shopping_cart

    def get_shipping_address(self):
        return self.shipping_address

    def get_has_subscribed(self):
        return self.has_subscribed

    # SETTERS
    def set_purchase_history(self, new_purchase_history):
        self.purchase_history = new_purchase_history

    def set_shopping_cart(self, new_shopping_cart):
        self.shopping_cart = new_shopping_cart

    def set_shipping_address(self, new_shipping_address):
        self.shipping_address = new_shipping_address

    def set_has_subscribed(self, new_has_subscribed):
        self.has_subscribed = new_has_subscribed

