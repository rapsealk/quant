pkg = c('magrittr', 'quantmod', 'rvest', 'httr', 'jsonlite',
        'readr', 'readxl', 'stringr', 'lubridate', 'dplyr',
        'tidyr', 'ggplot2', 'corrplot', 'dygraphs',
        'highcharter', 'plotly', 'PerformanceAnalytics',
        'nloptr', 'quadprog', 'RiskPortfolios', 'cccp',
        'timetk', 'broom', 'stargazer', 'timeSeries')

new.pkg = pkg[!(pkg %in% installed.packages()[, "Package"])]
if (length(new.pkg)) {
    install.packages(new.pkg, dependencies = TRUE)
}

library('magrittr')

x = c(0.3078, 0.2577, 0.5523, 0.0564, 0.4685,
      0.4838, 0.8124, 0.3703, 0.5466, 0.1703)

x %>% log() %>% diff() %>% exp() %>% round(., 2)

# DataFrame
number = data.frame(1, 2, 3, "4", 5, stringAsFactors = FALSE)
str(number)

for (i in number) {
    tryCatch({
        print(i^2)
    }, warning = function(w) {
        print(paste('Warning:', i))
    }, error = function(e) {
        print(paste('Error:', i))
    })
}
"
url.aapl = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL/data.csv?api_key=xw3NU3xLUZ7vZgrz5QnG'
data.aapl = read.csv(url.aapl)
head(data.aapl)

# 3.2.1 주가 다운로드
library(quantmod)
getSymbols('AAPL',
           from = '2000-01-01', to = '2020-03-21',
           auto.assign = FALSE)
head(AAPL)
chart_Series(Ad(AAPL))

ticker = c('FB', 'NVDA')
getSymbols(ticker)
head(FB)
head(NVDA)

# 3.2.2 국내 종목 주가 다운로드
getSymbols('005930.KS',
           from = '2000-01-01', to = '2020-03-21')
tail(Ad(`005930.KS`))
tail(Cl(`005930.KS`))

getSymbols('068760.KQ',
           from = '2000-01-01', to = '2020-03-21')
tail(Cl(`068760.KQ`))

# 3.2.3 FRED 데이터 다운로드 (Federal Reverse Economic Data)
getSymbols('DGS10', src = 'FRED')
chart_Series(DGS10)

getSymbols('DEXKOUS', src = 'FRED')
tail(DEXKOUS)
"
# 4.2.1 금융 속보 크롤링
library(httr)
library(rvest)

Sys.setlocale("LC_ALL", "English")

url = 'https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258'
data = GET(url)
print(data)

data_title = data %>%
             read_html(encoding = 'EUC-KR') %>%
             html_nodes('dl') %>%
             html_nodes('.articleSubject') %>%
             html_nodes('a') %>%
             html_attr('title')

Sys.setlocale("LC_ALL", "Korean")

print(data_title)

# 4.2.2 기업공시채널에서 오늘의 공시 불러오기
Sys.setlocale("LC_ALL", "English")

url = 'http://kind.krx.co.kr/disclosure/todaydisclosure.do'
data = POST(url, body = list(
    method = 'searchTodayDisclosureSub',
    currentPageSize = '15',
    pageIndex = '1',
    orderMode = '0',
    orderStat = 'D',
    forward = 'todaydisclosure_sub',
    chose = 'S',
    todayFlag = 'Y',
    selDate = '2018-12-28'
))
data = read_html(data) %>%
       html_table(fill = TRUE) %>%
       .[[1]]

Sys.setlocale("LC_ALL", "Korean")

print(head(data))