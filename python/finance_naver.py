#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/item/main.nhn?code="
stock_code = "005930"


def get_current_price(stock_code):
    result = requests.get(URL + stock_code)
    soup = BeautifulSoup(result.content, "html.parser")
    no_today = soup.find("p", {"class": "no_today"})
    now_price = no_today.find("span", {"class": "blind"})
    return now_price.text


print(get_current_price(stock_code))