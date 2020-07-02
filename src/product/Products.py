from dotenv import load_dotenv
import os


# singleton
class Products:
    def __init__(self):
        load_dotenv()
        self.size = int(os.getenv("PRODUCTS_SIZE"))
        self.values = [0] * self.size

    def get_values(self):
        return self.values

    def minus(self, index, value):
        self.values[index] -= value
        print(self.values)
        if self.values[index] < 0:
            raise RuntimeError("product value at " + str(index) + " is below 0 (" + self.values[index] + ")")

    def add(self, index, value):
        self.values[index] += value
        print(self.values)