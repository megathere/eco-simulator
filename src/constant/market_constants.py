import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

labor_size = int(os.getenv("LABOR_SIZE"))
product_size = int(os.getenv("PRODUCTS_SIZE"))

labor_value_vec = np.random.randint(low=1, high=10, size=labor_size)
product_value_vec = np.random.randint(low=1, high=10, size=product_size)

print("labor value vec: " + str(labor_value_vec))
print("product value vec: " + str(product_value_vec))