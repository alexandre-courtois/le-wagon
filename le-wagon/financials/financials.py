 # pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function
import math 

def forward_price(spot, interest_rate, time):
    forward = spot * math.exp(interest_rate * time)
    return round(forward,2)

# TODO: 2nd exercise: Define the `short_pnl` function

def short_pnl(positions, mtm):
    pnl = 0
    for strike_price, market_prices in enumerate(positions):
        pnl += (strike_price - market_prices)
    return pnl