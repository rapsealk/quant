#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Python porting of R package: PerformanceAnalytics (https://rdrr.io/cran/PerformanceAnalytics/src/R/Return.calculate.R)
"""
import unittest

import pandas as pd

from quant import get_symbols

__author__ = "rapsealk"
__version__ = "0.1.0"


def calculate_return(prices, method=['discrete', 'log', 'difference']):
    """
    Calculate returns from a prices stream
    ---
    prices: pandas.dataframe containing ordered price observations.
    Rm: rate of return of the market
    Ri: rate of return of the item
    """
    if type(method) is list:
        method = method[0]

    # if method == 'discrete':
    #     returns = prices

    close_prices = prices["Close"]

    dates = prices["Date"].tolist()
    kospi_close_prices = get_symbols(start=dates[0], end=dates[-1])["Close"]

    return_i = [
        (prices[1] - prices[0]) / prices[0] * 100
        for prices in zip(close_prices[:-1], close_prices[1:])
    ]

    return_m = [
        (prices[1] - prices[0]) / prices[0] * 100
        for prices in zip(kospi_close_prices[:-1], kospi_close_prices[1:])
    ]

    return_i = pd.DataFrame({"Date": dates[1:], "Close": return_i})
    return_m = pd.DataFrame({"Date": dates[1:], "Close": return_m})

    return (return_i, return_m)


class QuantTest(unittest.TestCase):

    def test_calculate_return(self):
        print('QuantTest.test_calculate_return *')
        samsung_electronics = get_symbols(code='005930.KS', start='2019-01-01', end='2019-12-31')
        ri, rm = calculate_return(samsung_electronics)
        self.assertTrue(len(ri) == len(rm))


if __name__ == "__main__":
    unittest.main()
