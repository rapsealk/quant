#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/item/main.nhn?code="
stock_code = "005930"


def get_kospi200():
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="  # page 1~20
    for i in range(20):
        response = None
        try:
            download_url = url + str(i+1)
            response = urllib.request.urlopen(download_url).read()
        except ValueError as e:
            sys.stderr.write('ValueError: {0}\n'.format(e))
            continue
        except urllib.error.URLError as e:
            sys.stderr.write('urllib.error.UrlError: {0} ({1})\n'.format(e, download_url))
            continue
        except urllib.error.HTTPError as e:
            sys.stderr.write('urllib.error.HTTPError: {0}\n'.format(e))
            continue
        except urllib.error.ContentTooShortError as e:
            sys.stderr.write('urllib.error.ContentTooShortError: {0}\n'.format(e))
            continue

        kospi200 = []

        if response:
            soup = BeautifulSoup(response, "html.parser")
            corporations = soup.find_all("td", {"class": "ctg"})
            for corporation in corporations:
                anchor = corporation.find("a")
                kospi200.append({
                    "name": anchor.text,
                    "code": anchor["href"].split('=')[-1]
                })

        return kospi200


def get_current_price(stock_code):
    result = requests.get(URL + stock_code)
    soup = BeautifulSoup(result.content, "html.parser")
    no_today = soup.find("p", {"class": "no_today"})
    now_price = no_today.find("span", {"class": "blind"})
    return now_price.text


print(get_current_price(stock_code))
