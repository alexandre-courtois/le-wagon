# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]

print(portfolio[3][0])

#fb_stocks_count = portfolio[3][0]-> Solution le wagon 
#print(fb_stocks_count) 

#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]   

pnl = 0

for i in range(len(portfolio)):
    volume, strike_price = portfolio[i]
    spot_price = market[i]
    pnl += volume * (spot_price - strike_price)

print(pnl)