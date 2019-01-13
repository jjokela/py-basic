# Compounding interest
# FV = PV * (1 + r)^t


def compound(present_value, interest_rate, time):
    return present_value * (1 + interest_rate) ** time


def compound_yearly_value(present_value, interest_rate, time):
    times = list(range(0, time + 1))
    return [compound(present_value, interest_rate, x) for x in times]


def compound_yearly_value_with_interest(present_value, interest_rate, time):
    times = list(range(0, time + 1))
    values = [compound(present_value, interest_rate, x) for x in times]
    interest_paid = [i - j for i, j in zip(values[1:], values[:-1])]
    interest_paid.insert(0, 0)
    result = zip(values, interest_paid)
    return list(result)
