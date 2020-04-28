#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from quant import get_symbols
from finance_naver import get_kospi200
from performance_analytics import calculate_return
from util import std

if __name__ == "__main__":
    kospi200 = get_kospi200()

    for corp in kospi200:
        corp["prices"] = get_symbols(code=corp["code"]+".KS", start='2019-01-01', end='2019-12-31')

    # print(kospi200, len(kospi200))
    for corp in kospi200:
        ri, rm = calculate_return(corp["prices"])
        # print(corp["name"], ri, rm)
        corp["std"] = std(ri["Rate"])
        print(corp["name"], corp["std"])
