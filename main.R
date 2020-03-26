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

# 4.2.3 네이버 금융에서 주식티커 크롤링
i = 0
ticker = list()
url = paste0('https://finance.naver.com/sise/',
             'sise_market_sum.nhn?sosok=', i, '&page=1')
down_table = GET(url)

navi.final = read_html(down_table, encoding = 'EUC-KR') %>%
             html_nodes(., '.pgRR') %>%
             html_nodes(., 'a') %>%
             html_attr(., 'href')
print(navi.final)

navi.final = navi.final %>%
             strsplit(., '=') %>%
             unlist() %>%
             tail(., 1) %>%
             as.numeric()
print(navi.final)

i = 0   # KOSPI
j = 1
url = paste0('https://finance.naver.com/sise/',
             'sise_market_sum.nhn?sosok=', i, '%page=', j)

Sys.setlocale("LC_ALL", "English")

table = read_html(down_table, encoding = 'EUC-KR') %>%
        html_table(fill = TRUE)
table = table[[2]]

Sys.setlocale("LC_ALL", "Korean")

print(head(table))

table[, ncol(table)] = NULL
table = na.omit(table)
print(head(table))

symbol = read_html(down_table, encoding = 'EUC-KR') %>%
         html_nodes(., 'tbody') %>%
         html_nodes(., 'td') %>%
         html_nodes(., 'a') %>%
         html_nodes(., 'href')
print(head(symbol, 10))

library(stringr)

symbol = sapply(symbol, function(x) {
    str_sub(x, -6, -1)
})
symbol = unique(symbol)
print(head(symbol, 10))

table$N = symbol
colnames(table)[1] = '종목코드'
rownames(table) = NULL
ticker[[j]] = table

data = list()

# i = 0 은 코스피, i = 1 은 코스닥 종목
for (i in 0:1) {

  ticker = list()
  url =
    paste0('https://finance.naver.com/sise/',
             'sise_market_sum.nhn?sosok=',i,'&page=1')
  
  down_table = GET(url)
  
  # 최종 페이지 번호 찾아주기
  navi.final = read_html(down_table, encoding = "EUC-KR") %>%
      html_nodes(., ".pgRR") %>%
      html_nodes(., "a") %>%
      html_attr(.,"href") %>%
      strsplit(., "=") %>%
      unlist() %>%
      tail(., 1) %>%
      as.numeric()
  
  # 첫번째 부터 마지막 페이지까지 for loop를 이용하여 테이블 추출하기
  for (j in 1:navi.final) {
    
    # 각 페이지에 해당하는 url 생성
    url = paste0(
      'https://finance.naver.com/sise/',
      'sise_market_sum.nhn?sosok=',i,"&page=",j)
    down_table = GET(url)
 
    Sys.setlocale("LC_ALL", "English")
    # 한글 오류 방지를 위해 영어로 로케일 언어 변경
 
    table = read_html(down_table, encoding = "EUC-KR") %>%
      html_table(fill = TRUE)
    table = table[[2]] # 원하는 테이블 추출
 
    Sys.setlocale("LC_ALL", "Korean")
    # 한글을 읽기위해 로케일 언어 재변경
 
    table[, ncol(table)] = NULL # 토론식 부분 삭제
    table = na.omit(table) # 빈 행 삭제
    
    # 6자리 티커만 추출
    symbol = read_html(down_table, encoding = "EUC-KR") %>%
      html_nodes(., "tbody") %>%
      html_nodes(., "td") %>%
      html_nodes(., "a") %>%
      html_attr(., "href")
 
    symbol = sapply(symbol, function(x) {
        str_sub(x, -6, -1) 
      })
    
    # 테이블에 티커 넣어준 후, 테이블 정리
    table$N = symbol
    colnames(table)[1] = "종목코드"

    rownames(table) = NULL
    ticker[[j]] = table
 
    Sys.sleep(0.5) # 페이지 당 0.5초의 슬립 적용
  }
  
  # do.call을 통해 리스트를 데이터 프레임으로 묶기
  ticker = do.call(rbind, ticker)
  data[[i + 1]] = ticker
}

# 코스피와 코스닥 테이블 묶기
data = do.call(rbind, data)