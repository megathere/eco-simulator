from src.product.Products import Products


class Labor:
    def __init__(self, index, p: Products):
        self.index = index
        self.p = p

    def consume(self):
        self.p.minus(self.index, 1)
