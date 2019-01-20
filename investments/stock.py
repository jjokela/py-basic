class Stock:
    def __init__(self, expected_return):
        self.expected_return = expected_return


class Portfolio:
    stocks = []

    def add(self, Stock, investment):
        self.stocks.append(Stock)



stocks = [
    Stock(.04),
    Stock(.02),
    Stock(.03)
]

investments = [
    10000,
    20000,
    5000
]

data = list(zip(stocks, investments))
print(data)

foo = [s.expected_return * i for s, i in zip(stocks, investments)]

print(foo)


# [x.expectedReturn * y for x,y in zip(Stocks,investments)]

