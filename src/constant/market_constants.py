from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
company_size = int(os.getenv("COMPANIES_SIZE"))

flow_stack = []

market_caps = []
for i in range(company_size):
    market_caps.append(np.random.randint(low=101, high=105))