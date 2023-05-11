
class Seller:
    id = int
    name = str
    last_name: str
    age = int
    email = str
    address = str
    city = str
    state = str
    postal_code = int
    number_phone = int
    activity_time = int
    sector_in_charge = str
    sales_made = int

    # return_policy > politica de devolicion
    # response_time > tiempo de respuesta
    # products
    # ratings > calificaiones
    # payment_methods
    # geographic_location
    # comments

    def __init__(self, id, name, age, last_name, address, city, state, postal_code, email, activity_time, number_phone, sector_in_charge, sales_made):
        self.id = id
        self.name = name
        self.age = age
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.email = email
        self.activity_time = activity_time
        self.number_phone = number_phone
        self.sector_in_charge = sector_in_charge
        self.sales_made = sales_made

