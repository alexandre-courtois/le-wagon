# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

#       vol  strike
aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
meta   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, meta ]

portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "META": {
    "volume": 18,
    "strike": 209.0
  }
}

print(portfolio['TSLA']['volume'])
print(portfolio['GOOG']['strike'])

market = {
  "AAPL":  198.84,
  "GOOG": 1217.93,
  "TSLA":  267.66,
  "META":    179.06
}


pnl = 0

for stock, values in portfolio.items():
    volume = values["volume"]
    strike = values["strike"]
    spot = market[stock]
    pnl += volume * (spot - strike)
    
print(pnl)


















