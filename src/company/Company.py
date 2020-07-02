from dotenv import load_dotenv

from src.constant.market_constants import product_value_vec, labor_value_vec
from src.product.Products import Products


class Company:
    def __init__(self, index, p: Products):
        load_dotenv()
        self.product_cost = product_value_vec[index]
        self.labor_cost = labor_value_vec[index]
        self.index = index
        self.p = p

    def produce(self):
        self.p.add(self.index, self.product_cost + self.labor_cost)

    def consume(self):
        self.p.minus(self.index, self.product_cost)
