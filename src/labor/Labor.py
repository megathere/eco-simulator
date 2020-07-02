from src.product.Products import Products
from src.constant.market_constants import labor_value_vec


class Labor:
    def __init__(self, index, value, p: Products):
        self.index = index
        self.value = labor_value_vec[index]
        self.p = p

    def consume(self):
        self.p.minus(self.index, self.value)

    def get_value(self):
        return self.value
