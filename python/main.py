#!/usr/bin/python3
# -*- coding: utf-8 -*-
from quant import get_symbols


def main():
    samsung_electronics = get_symbols(code='005930.KS', start='2019-01-01', end='2020-03-17')
    print(samsung_electronics)


if __name__ == "__main__":
    main()
