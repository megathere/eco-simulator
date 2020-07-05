import numpy as np
from dotenv import load_dotenv
import os


def get_product_to_labor_vec(p_v_sum):
    vec = [0]*len(p_v_sum)
    for i in range(len(p_v_sum)):
        vec[i] = np.random.randint(low=0, high=p_v_sum[i])
    return vec

load_dotenv()

labor_size = int(os.getenv("LABOR_SIZE"))
product_size = int(os.getenv("PRODUCTS_SIZE"))

labor_value_vec = np.random.randint(low=5, high=20, size=labor_size)
labor_value_sum = sum(labor_value_vec)
print("labor value vec: " + str(labor_value_vec) + ", sum: " + str(labor_value_sum))
print()

cost_value_vec = np.random.randint(low=5, high=80, size=product_size)
cost_value_sum = sum(cost_value_vec)
print("cost value vec: " + str(cost_value_vec) + ", sum: " + str(cost_value_sum))
print()

product_value_vec = np.add(labor_value_vec, cost_value_vec)
product_value_sum = sum(product_value_vec)
print("product value vec: " + str(product_value_vec) + ", sum: " + str(product_value_sum))
print()

product_value_min = min(product_value_vec)
print("product value min: " + str(product_value_min))
print()

product_to_labor_vec = get_product_to_labor_vec(product_value_vec)
product_to_product_vec = np.subtract(product_value_vec, product_to_labor_vec)
print("product-to-labor vec: " + str(product_to_labor_vec))
print("product-to-product vec: " + str(product_to_product_vec))
print()
