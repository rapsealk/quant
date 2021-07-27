import pandas as pd


class KRXProvider:

    def __init__(self):
        pass

    def get_corporations(self):
        df_corps = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
        return df_corps


if __name__ == "__main__":
    pass
