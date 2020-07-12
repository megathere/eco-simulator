import numpy as np


# scenarios:
# 1. same margin, less re-investment rate means less profit but more market share (value)

class Company:
    def __init__(self, index):
        self.index = index
        # self.value = np.random.randint(low=10, high=100)
        self.value = 100
        # self.productivity = 1 + np.random.randint(low=0, high=5) / 100
        self.p_margin = 0.01
        # self.p_labor = np.random.randint(low=0, high=10) / 10
        self.p_labor = 0.5
        self.p_product = 1 - self.p_labor
        self.p_re_investment = np.random.randint(low=0, high=100) / 100
        self.profit = 0
        self.init_p()

    def operate(self):
        margin = self.value * self.p_margin
        margin_to_investment = margin * self.p_re_investment
        margin_to_profit = margin - margin_to_investment

        self.value = self.value + margin_to_investment
        self.profit = self.profit + margin_to_profit

    def init_p(self):
        print(str(self.index) + " -> Margin Rate:\t" + "{:.2f}".format(self.p_margin))
        print(str(self.index) + " -> Re-Investment Rate:\t" + "{:.2f}".format(self.p_re_investment))

    def p(self):
        print(str(self.index) + " -> Value:\t" + "{:.2f}".format(self.value))
        print(str(self.index) + " -> Profit:\t" + "{:.2f}".format(self.profit))

    def get_value(self):
        return self.value

    def get_profit(self):
        return self.profit