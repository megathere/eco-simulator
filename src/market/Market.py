import os

from dotenv import load_dotenv
from termcolor import colored

from src.company.Company import Company
from src.constant import market_constants


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
            self.p_before_i(ii)
            for company in self.c:
                company.operate()
            self.p_after_i()

    def p_before_i(self, iter):
        print()
        print("----------- Iteration " + colored(str(iter), 'red') + " ----------")

    def p_after_i(self):

        sum_value = 0
        sum_profit = 0
        for company in self.c:
            company.p()
            sum_value = sum_value + company.get_value()
            sum_profit = sum_profit + company.get_profit()

        print("M -> Bank Balance:\t" + "{:.3f}".format(market_constants.bank_balance))
        print("M -> Value:\t\t" + "{:.3f}".format(sum_value))
        print("M -> Profit:\t" + "{:.3f}".format(sum_profit))
        print("M -> Margin:\t\t" + str(["{:.3f}".format(p) for p in market_constants.market_margin]))
