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

    def __init__(self, id:str, name: str, last_name: str, age: int, address: str, city: str,
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

    # hacer setter y getter

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

