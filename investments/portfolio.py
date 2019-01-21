class Investment(object):
    def __init__(self, identifier, amount, price):
        self.identifier = identifier
        self.amount = amount
        self.original_price = price
        self.price = price

    def value(self):
        return self.amount * self.price

    def investment_return(self):
        return self.price / self.original_price - 1

    def print(self):
        print('Name:', self.identifier, 'value:', self.value(), 'return:', self.investment_return(), 'original price',
              self.original_price)


inv = Investment(identifier='Apple', amount=100, price=20)
inv.print()
inv.price = 30
inv.print()


class Portfolio(object):
    def __init__(self, investments):
        self.investments = investments

    def portfolio_return(self):
        weights = map(lambda x: x.value() / self.value(), self.investments)
        returns = map(lambda x: x.investment_return(), self.investments)
        weight_return = zip(weights, returns)
        return sum(map(lambda x: (x[0] * x[1]), weight_return))

    def weights(self):
        names = list(map(lambda x: x.identifier, self.investments))
        weights = list(map(lambda x: x.value() / self.value(), self.investments))
        return list(zip(names, weights))

    def value(self):
        investments_sum = 0
        for i in self.investments:
            investments_sum += i.value()
        return investments_sum


investment_1 = Investment(identifier='Apple', amount=100, price=20)
investment_2 = Investment(identifier='M$', amount=200, price=15)
investment_3 = Investment(identifier='Amazon', amount=600, price=12)
investments = [investment_1, investment_2, investment_3]

print(investment_3.investment_return())

pofo = Portfolio(investments)

investment_1.price = 15
investment_2.price = 17
investment_3.price = 20

print('pofo total value', pofo.value())
[i.print() for i in pofo.investments]
print(pofo.weights())
print('pofo return', pofo.portfolio_return())
