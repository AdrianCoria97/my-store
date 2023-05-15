from datetime import datetime
from domain.Client import Client


class Seller(Client):
    activity_time = datetime
    sector_in_charge = str
    sales_made = int

    def __init__(self, activity_time: datetime, sector_in_charge: str, sales_made: int, id: str, name: str,
                 last_name: str, age: int, address: str, city: str, state: str, zip_code: str, phone: str,
                 email: str, status: bool):

        # Con super llamamos a los metodos de la clase padre
        super().__init__(id, name, last_name, age, address, city, state, zip_code, phone, email, status)
        self.activity_time = activity_time
        self.sector_in_charge = sector_in_charge
        self.sales_made = sales_made

    # GETTERS
    def get_activity_time(self):
        return self.activity_time

    def get_sector_in_charge(self):
        return self.sector_in_charge

    def get_sales_made(self):
        return self.sales_made

    # SETTERS
    def set_activity_time(self, new_activity_time):
        self.activity_time = new_activity_time

    def set_sector_in_charge(self, new_sector_in_charge):
        self.sector_in_charge = new_sector_in_charge

    def set_sales_made(self, new_sales_made):
        self.sales_made = new_sales_made

