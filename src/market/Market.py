from dotenv import load_dotenv
import os
from termcolor import colored

from src.company.Company import Company


class Market:
    def __init__(self):
        load_dotenv()
        self.company_size = int(os.getenv("COMPANIES_SIZE"))
        self.iter_size = int(os.getenv("ITERATION_SIZE"))

        self.c = []
        for i in range(self.company_size):
            self.c.append(Company(i))

    def operate(self):
        for ii in range(self.iter_size):
            print()
            print("----------- Iteration " + colored(str(ii), 'red') + " ----------")
            sum_value = 0
            sum_profit = 0
            for company in self.c:
                company.operate()
                # company.p()
                sum_value = sum_value + company.get_value()
                sum_profit = sum_profit + company.get_profit()
            print("Total Value:\t" + "{:.2f}".format(sum_value))
            print("Total Profit:\t" + "{:.2f}".format(sum_profit))