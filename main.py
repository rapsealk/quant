#!/usr/bin/python3
# -*- coding: utf-8 -*-
# from quant import get_symbols
# from finance_naver import get_kospi200
from quant.providers import NaverFinanceProvider
from quant.quant import get_corporations


def main():
    # kospi200 = get_kospi200()
    # print(kospi200)
    print(NaverFinanceProvider().get_kospi200())
    # print(NaverFinanceProvider().get_current_price())
    corps = get_corporations()
    print(corps)


if __name__ == "__main__":
    main()
