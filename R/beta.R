#!/usr/local/bin/Rscript
pkg = c('magrittr', 'quantmod', 'PerformanceAnalytics')

new.pkg = pkg[!(pkg %in% installed.packages()[, "Package"])]
if (length(new.pkg)) {
    install.packages(new.pkg, dependencies = TRUE, repos="http://healthstat.snu.ac.kr/CRAN/")
}

library(quantmod)
library(PerformanceAnalytics)
library(magrittr)

symbols = c('102110.KS', '039490.KS')
getSymbols(symbols)

prices = do.call(cbind, lapply(symbols, function(x) Cl(get(x))))

ret = Return.calculate(prices)
ret = ret['2016-01::2018-12']

rm = ret[, 1]
ri = ret[, 2]

reg = lm(ri ~ rm)
summary(reg)