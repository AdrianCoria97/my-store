from datetime import datetime
from domain.Client import Client


class Seller(Client):
    activity_time = datetime
    sector_in_charge = str
    sales_made = int

    def __init__(self, activity_time, sector_in_charge, sales_made, id: str, name: str, last_name: str, age: int,
                 address: str, city: str, state: str, zip_code: str, phone: str, email: str, status: bool):

        # Con super llamamos a los metodos de la clase padre
        super().__init__(id, name, last_name, age, address, city, state, zip_code, phone, email, status)
        self.activity_time = activity_time
        self.sector_in_charge = sector_in_charge
        self.sales_made = sales_made

