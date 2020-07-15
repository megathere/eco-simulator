from src.constant import market_constants


class Company:
    def __init__(self, index):
        self.index = index
        # self.value = np.random.randint(low=10, high=100)
        self.value = 100
        self.margin_coefficient = market_constants.market_margin_coefficient[index]
        # self.p_margin = 0.01
        # self.p_labor = np.random.randint(low=0, high=10) / 10
        self.p_labor = 0.5
        self.p_product = 1 - self.p_labor
        self.p_re_investment = 0.5
        self.profit = 0

        self.p()

    def get_margin(self):
        return self.margin_coefficient / self.value

    def operate(self):
        margin = self.value * self.get_margin()
        market_constants.market_margin[self.index] = self.get_margin()

        if self.get_margin() < max(market_constants.market_margin):
            margin *= 0.8
            market_constants.bank_balance += margin / 4
        else:
            if market_constants.bank_balance > 10:
                market_constants.bank_balance -= 10
                self.value += 10

        self.value += margin * self.p_re_investment
        self.profit += margin * (1 - self.p_re_investment)

    def p(self):
        print(str(self.index) + " -> Margin:\t" + "{:.3f}".format(self.get_margin()))
        print(str(self.index) + " -> Value:\t\t" + "{:.3f}".format(self.value))
        print(str(self.index) + " -> Profit:\t" + "{:.3f}".format(self.profit))
        # print(str(self.index) + " -> Re-Investment Rate:\t" + "{:.3f}".format(self.p_re_investment))
        print()

    def get_value(self):
        return self.value

    def get_profit(self):
        return self.profit
