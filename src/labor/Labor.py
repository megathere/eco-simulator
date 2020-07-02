from src.product.Products import Products


class Labor:
    def __init__(self, index, value, p: Products):
        self.index = index
        self.value = value
        self.p = p

    def consume(self):
        self.p.minus(self.index, self.value)

    def get_value(self):
        return self.value