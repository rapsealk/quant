#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import sys
import time
from datetime import datetime

import pandas as pd

import unittest


HTTP_200_OK = 200


def get_corporations():
    df_corps = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
    print(df_corps.head())
    return df_corps


def get_symbols(code='005930.KS', start='2000-01-01', end=None, save_as=None):
    """
    start: yyyy-MM-dd
    end: yyyy-MM-dd
    ---
    period1: gap between 1970-01-01 and start in SECONDS
    period2: gap between 1970-01-01 and end in SECONDS
    """
    if end is None:
        end = datetime.now().strftime('%Y-%m-%d')

    base_url = 'https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}&period2={2}&interval=1d&events=history'
    # url = 'https://finance.yahoo.com/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter=history&frequency=1d'
    period1 = int(_get_local_timestamp(start))
    period2 = int(_get_local_timestamp(end))

    assert period1 <= period2

    download_url = base_url.format(code, period1, period2)

    """ Download csv file from Yahoo Finance.
    filename = './{0}.csv'.format(code)
    try:
        urllib.request.urlretrieve(download_url.format(code, period1, period2), filename)
    except ValueError as e:
        print('ValueError:', e)
        return None
    except urllib.error.URLError as e:
        print('urllib.error.URLError:', e)
        return None

    # Read and process the data.
    fhandle = open(filename, 'r')
    data = list(map(lambda x: x.replace('\n', '').split(','), fhandle.readlines()))
    print(data, len(data))
    fhandle.close()

    # Remove the file.
    if os.path.exists(filename):
        os.remove(filename)
    """
    try:
        result = requests.get(download_url)
        if result.status_code != HTTP_200_OK:
            sys.stderr.write('HTTP Status Code: {0} ({1})'.format(result.status_code, download_url))
    except requests.exceptions.MissingSchema as e:
        sys.stderr.write('requests.exceptions.MissingSchema: {0}\n'.format(e))
        return None
    except requests.exceptions.InvalidURL as e:
        sys.stderr.write('requests.exceptions.InvalidURL: {0}\n'.format(e))
        return None

    if save_as is not None and type(save_as) is str:
        fhandle = open(save_as, 'w')
        fhandle.write(result.content.decode("utf-8"))
        fhandle.close()

    data = list(map(lambda x: x.split(','), result.content.decode("utf-8").split('\n')))

    return data

    """
    result = requests.get(url)
    if result.status_code != HTTP_200_OK:
        print('Failed to get {}: {}'.format(result.status_code, url))
        return None

    soup = BeautifulSoup(result.content, "html.parser")
    # print(result.content)
    table_records = soup.find_all("tr", {"class": "BdT"})
    # table_records = list(filter(lambda x: x is not None, map(lambda x: x.find("span"), table_records)))
    print(table_records, len(table_records))
    """


def _get_local_timestamp(date_str='2000-01-01'):
    offset_in_seconds = 9 * 60 * 60
    return time.mktime(time.strptime(date_str, '%Y-%m-%d')) + offset_in_seconds


class QuantTest(unittest.TestCase):

    def test_local_timestamp(self):
        timestamp = _get_local_timestamp('2019-03-26')
        self.assertEqual(timestamp, 1553558400)


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--abc', action='store_true', default=False)
    args = parser.parse_args()

    if args.abc:
    """
    unittest.main()
