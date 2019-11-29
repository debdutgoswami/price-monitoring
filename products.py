class Product:
    name: str = None
    price: float = None
    def __init__(self,name=None, price=None):
        self.name = name
        self.price = price