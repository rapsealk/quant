#!/usr/bin/python3
# -*- coding: utf-8 -*-
from quant import get_symbols
from finance_naver import get_kospi200


def main():
    kospi200 = get_kospi200()
    print(kospi200)


if __name__ == "__main__":
    main()
