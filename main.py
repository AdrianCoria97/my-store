from domain.Article import Article
import uuid
from datetime import datetime
from domain.Buyer import Buyer

if __name__ == '__main__':
    first_buyer = Buyer(purchase_history=[], shopping_cart=[], shipping_address="Calle none 123", has_subscribed=True,
                        id=str(uuid.uuid4()), name="Mauricio", last_name="Pizarro", age=26, address="La Colonia",
                        city="Mendoza", zip_code="5572", phone="2634773945", email="maurigato@gmail.com", status=True)

    first_article = Article(id=str(uuid.uuid4()), name= "Philco", item_id=1, description="TV Smart",
                            category="Electrodomesticos", price=100000.00, stock=3, seller=first_buyer,
                            average_rating=10, comments=["Muy Bueno", "Exelente"], date_created=datetime.now(),
                            shipping_methods=["Andreani", "Envio Express"], buyer=first_buyer)

    print(first_article.__dict__)
    print(first_buyer.__dict__)
