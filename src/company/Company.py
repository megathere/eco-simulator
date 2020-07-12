from src.constant import market_constants


class Company:
    def __init__(self, index):
        self.index = index
        # self.value = np.random.randint(low=10, high=100)
        self.value = 100
        self.p_margin = market_constants.market_caps[index] / 100 - 1
        # self.p_margin = 0.01
        # self.p_labor = np.random.randint(low=0, high=10) / 10
        self.p_labor = 0.5
        self.p_product = 1 - self.p_labor
        self.p_re_investment = 0.5
        self.profit = 0

        self.p()

    def operate(self):
        margin = self.value * self.p_margin
        margin_to_investment = margin * self.p_re_investment
        margin_to_profit = margin - margin_to_investment

        # print(str(self.index) + " -> margin_to_investment:\t" + "{:.3f}".format(margin_to_investment))
        # print(str(self.index) + " -> margin_to_profit:\t" + "{:.3f}".format(margin_to_profit))

        self.value = self.value + margin_to_investment
        self.profit = self.profit + margin_to_profit

        # self.add_value(self.index, 1)

    def p(self):
        print(str(self.index) + " -> Margin:\t" + "{:.3f}".format(self.p_margin))
        print(str(self.index) + " -> Value:\t\t" + "{:.3f}".format(self.value))
        print(str(self.index) + " -> Profit:\t" + "{:.3f}".format(self.profit))
        # print(str(self.index) + " -> Re-Investment Rate:\t" + "{:.3f}".format(self.p_re_investment))
        print()

    def get_value(self):
        return self.value

    def add_value(self, index, v):
        market_constants.flow_stack.append((index, 0, v))
        print(str(market_constants.flow_stack))

    def abstract_value(self, v):
        self.value -= v

    def get_profit(self):
        return self.profit
