from Domain import Product
from App import db

class ProductModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def create(data: Product):
        return ProductModel(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )

    def toProduct(self):
        return Product(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price
        )

    def toJSON(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
