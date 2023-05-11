class Article:
    id_product = int
    name: str
    item_id: int
    description: str
    category: str
    price: float
    availability: int
    seller: str
    average_rating: float
    comments: [str]
    images: [str]
    features: [str, str]
    ratings: [float]
    publication_date: str
    status: str
    shipping_methods: [str]

    def __init__(self, id_product, name, item_id, description, category, price, availability, seller, average_rating, comments,
                 images, features, ratings, publication_date, status, shipping_methods):
        self.id_product = id_product
        self.name = name
        self.item_id = item_id
        self.description = description
        self.category = category
        self.price = price
        self.availability = availability
        self.seller = seller
        self.average_rating = average_rating
        self.comments = comments
        self.images = images
        self.features = features
        self.ratings = ratings
        self.publication_date = publication_date
        self.status = status
        self.shipping_methods = shipping_methods
