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

