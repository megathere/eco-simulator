import unittest

from src.market.Market import Market


class Test(unittest.TestCase):
    def test_products(self):
        m = Market()
        m.operate_all()


if __name__ == '__main__':
    unittest.main()
