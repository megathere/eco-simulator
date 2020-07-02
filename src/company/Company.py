from dotenv import load_dotenv
import os

from src.labor.Labor import Labor
from src.product.Products import Products


class Company:
    def __init__(self, index, p: Products, l:Labor):
        load_dotenv()
        self.cost = int(os.getenv("PRODUCTS_COST_VALUE"))
        self.index = index
        self.p = p
        self.l = l

    def produce(self):
        self.p.add(self.index, self.cost + self.l.get_value())

    def consume(self):
        self.p.minus(self.index, self.cost)
