class Client:
    id: str
    name: str
    last_name: str
    age: int
    address: str
    city: str
    zip_code: str
    phone: str
    email: str
    status: bool

    def __init__(self, id: str, name: str, last_name: str, age: int, address: str, city: str,
                 zip_code: str, phone: str, email: str, status: bool):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.phone = phone
        self.email = email
        self.status = status

    # GETTERS
    def get_name_client(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_zip_code(self):
        return self.zip_code

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_status(self):
        return self.status

    # SETTERS
    def set_name_client(self, new_name):
        self.name = new_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_age(self, new_age):
        self.age = new_age

    def set_address(self, new_address):
        self.address = new_address

    def set_city(self, new_city):
        self.city = new_city

    def set_zip_code(self, new_zip_code):
        self.zip_code = new_zip_code

    def set_phone(self, new_phone):
        self.phone= new_phone

    def set_email(self, new_email):
        self.email = new_email

    def set_status(self, new_status):
        self.status = new_status
