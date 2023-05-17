from domain.Article import Article
import uuid
from datetime import datetime
from domain.Buyer import Buyer
from domain.Seller import Seller
from domain.Store import Store

if __name__ == '__main__':
    first_buyer = Buyer(purchase_history=["carting", "carpa para 4 personas"], shopping_cart=["Llave 10", "amoladora"],
                        has_subscribed=True, id=str(uuid.uuid4()), name="Mauricio", last_name="Pizarro", age=26,
                        address="La Colonia", city="Mendoza", zip_code="5572", phone="2634773945",
                        email="mauriciopi.14@gmail.com", status=True)

    first_seller = Seller(activity_time=datetime.now(), sector_in_charge="Panaderia", sales_made=25,
                          id=str(uuid.uuid4()), name="Alejandro", last_name="Steffen", age=46, address="Palmira",
                          city="Mendoza", zip_code="5573", phone="2634778533", email="steffen.ale@gmail.com",
                          status=False)

    first_article = Article(id=str(uuid.uuid4()), name="Philco", item_id=1, description="TV Smart",
                            category="Electrodomesticos", price=100000.00, stock=3, seller=first_seller,
                            buyer=first_buyer, date_created=datetime.now())

    # add buyer ?
    list_products = [first_article]
    list_seller = [first_seller]
    first_store = Store(id=str(uuid.uuid4()), store_name="La saladita express",
                        products=list_products, employees=list_seller,
                        sales_of_the_month=25)

    print(first_buyer.__dict__)
    print(first_seller.__dict__)
    print(first_article.__dict__)
    print(first_store.__dict__)


