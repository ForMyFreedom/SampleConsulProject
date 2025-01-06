class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

class InfraResponse:
    def __init__(self, data, error):
        self.data = data
        self.error = error
