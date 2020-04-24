#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.linear_model import LinearRegression

from quant import get_symbols
from performance_analytics import calculate_return


def linear_regression(data, y_var, x_vars):
    y = data[y_var]
    x = data[x_vars]
    lin_reg = LinearRegression()
    model = lin_reg.fit(x, y)
    return [model.intercept_, model.coef_]


def main():
    tiger200etf = '102110.KS'
    kiwoom = get_symbols('039490.KS', start='2016-01-01', end='2018-12-31')

    ri, rm = calculate_return(kiwoom, tiger200etf)
    print(ri)
    print(rm)

    lin_reg = LinearRegression()
    ri_rate = np.array(ri["Rate"].tolist())
    ri_rate = np.reshape(ri_rate, newshape=(-1, 1))
    rm_rate = np.array(rm["Rate"].tolist())
    rm_rate = np.reshape(rm_rate, newshape=(-1, 1))
    model = lin_reg.fit(rm_rate, ri_rate)

    beta = model.coef_[0, 0]
    print('beta:', beta)


if __name__ == "__main__":
    main()
