
class Store:
    id: str
    store_name: str
    attention_schedule: int
    products: list
    employees: dict
    sales_of_the_month: int
    return_policy:str
    response_time: str
    ratings: int
    payment_methods: str
    comments: list
    geographic_location: str

    def __init__(self, id: str, store_name: str, attention_schedule: int, products: list, employees: dict,
                 sales_of_the_month: int, return_policy:str, response_time: str, ratings: int, payment_methods: str,
                 comments: list, geographic_location: str):
        self.id = id
        self.store_name = store_name
        self.attention_schedule = attention_schedule
        self.products = products
        self.employees = employees
        self.sales_of_the_month = sales_of_the_month
        self.return_policy = return_policy
        self.response_time = response_time
        self.ratings = ratings
        self.payment_methods = payment_methods
        self.comments = comments
        self.geographic_location = geographic_location

    # GETTERS
    def get_store(self):
        return self.store_name

    def get_attention_schedule(self):
        return self.attention_schedule

    def get_products(self):
        return self.products

    def get_employees(self):
        return self.employees

    def get_sales_of_the_month(self):
        return self.sales_of_the_month

    def get_return_policy(self):
        return self.return_policy

    def get_response_time(self):
        return self.response_time

    def get_ratings(self):
        return self.ratings

    def get_payment_methods(self):
        return self.payment_methods

    def get_comments(self):
        return self.comments

    def get_geographic_location(self):
        return self.geographic_location

    # SETTERS
    def set_store_name(self, new_store_name):
        self.store_name = new_store_name

    def set_attention_schedule(self, new_attention_schedule):
        self.attention_schedule = new_attention_schedule

    def set_products(self, new_products):
        self.products = new_products

    def set_employees(self, new_employees):
        self.employees = new_employees

    def set_sales_of_the_month(self, new_sales_of_the_month):
        self.sales_of_the_month = new_sales_of_the_month

    def set_return_policy(self, new_return_policy):
        self.return_policy = new_return_policy

    def set_response_time(self, new_response_time):
        self.response_time = new_response_time

    def set_ratings(self, new_ratings):
        self.ratings = new_ratings

    def set_payment_methods(self, new_payment_methods):
        self.payment_methods = new_payment_methods

    def set_comments(self, new_comments):
        self.comments = new_comments

    def set_geographic_location(self, new_geographic_location):
        self.geographic_location = new_geographic_location

