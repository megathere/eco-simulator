from dotenv import load_dotenv
import os

from src.company.Company import Company
from src.labor.Labor import Labor
from src.product.Products import Products


class Market:
    def __init__(self):
        load_dotenv()
        self.company_size = int(os.getenv("COMPANIES_SIZE"))
        self.labor_size = int(os.getenv("LABOR_SIZE"))
        self.iter_size = int(os.getenv("ITERATIONS"))
        self.labor_value = int(os.getenv("LABOR_VALUE"))
        self.p = Products()

        self.l = []
        for i in range(self.labor_size):
            self.l.append(Labor(i, self.labor_value, self.p))

        self.c = []
        for i in range(self.company_size):
            self.c.append(Company(i, self.p, self.l[i]))

    def operate_all(self):
        for i in range(self.iter_size):
            self.operate(i)

    def operate(self, index):
        print("iteration " + str(index))
        print("START: " + str(self.p.get_values()))
        for company in self.c:
            company.produce()
        for labor in self.l:
            labor.consume()
        for company in self.c:
            company.consume()
        print("END: " + str(self.p.get_values()))
