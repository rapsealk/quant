# Quant
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)![R 4.0.0](https://img.shields.io/badge/R-4.0.0-yellow.svg)

* [R을 이용한 퀀트 투자 포트폴리오 만들기](https://hyunyulhenry.github.io/quant_cookbook/)

## Personal Library Path
* C:\Users\$USERNAME\Documents/R/win-library/3.6

## Data
* [Yahoo Finance](https://finance.yahoo.com/)

## Backgrounds
* CAPM (자본자산가격결정모형): Capital Asset Pricing Model
    - 증권을 비롯한 자본자산의 위험과 수익 사이에 존재하는 균형관계를 설명하기 위한 모형
    - 모든 투자자가 효율적 분산투자의 원리에 따라 행동하는 경우 개별증권 또는 포트폴리오의 위험과 수익은 어떠한 관계를 갖는가를 설명하는 모형
    - 이 모형은 시장 및 시장참가자에 대해 아래와 같은 가정을 한다.
        - 투자자가 투자를 결정할 때의 결정기준은 수익률은 평균과 표준 편차이며(수익률이 정규분포이거나 투자자의 효용함수가 2차 함수임을 가정한다.), 평균은 높을수록 표준편차는 낮을수록 선호도가 높다.
        - 증권이 거래되는 자본시장은 완전경쟁적 시장으로서 (1) 시장참가자는 개별적으로 시장가격(수익률) 형성에 전혀 영향을 미치지 못하고, (2) 일체의 거래비용은 0이며, (3) 필요한 모든 정보는 무료로 모든 시장 참가자에게 동시적으로 공급된다.
        - 투자가들의 수익률분포에 대한 예측은 동일하다.
        - 시장에는 무위험자산이 존재하며 차입과 대출이 자유롭다.
    - 이러한 가정하에 CAPM을 유도하면 개별증권의 기대수익률은 쳬게적 위험의 선형증가함수가 되어, 다음 선형관계식이 성립한다.
    ```
    Ri = Rf + βi * [Rm - Rf]
    * Ri: 개별 주식의 수익률
    * Rf: 무위험 수익률
    * βi: 개별 주식의 베타
    * Rm - Rf: 시장위험 프리미엄
    ```
