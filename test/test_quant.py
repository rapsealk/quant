import unittest

from quant import get_symbols, get_local_timestamp, calculate_return


class QuantTest(unittest.TestCase):

    def test_local_timestamp(self):
        timestamp = get_local_timestamp('2019-03-26')
        self.assertEqual(timestamp, 1553558400)

    def test_calculate_return(self):
        samsung_electronics = get_symbols(code='005930.KS', start='2019-01-01', end='2019-12-31')
        ri, rm = calculate_return(samsung_electronics)
        self.assertTrue(len(ri) == len(rm))


if __name__ == "__main__":
    unittest.main()
