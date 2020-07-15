from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
company_size = int(os.getenv("COMPANIES_SIZE"))

flow_stack = []

market_margin = [0] * company_size
# coefficient = value * margin
# value up, margin down
market_margin_coefficient = []
for i in range(company_size):
    market_margin_coefficient.append(np.random.randint(low=100, high=500) / 100)

bank_balance = 0
