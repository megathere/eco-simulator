from src.product.Products import Products


class Company:
    def __init__(self, index, p: Products):
        self.index = index
        self.p = p

    def produce(self):
        self.p.add(self.index, 2)

    def consume(self):
        self.p.minus(self.index, 1)
