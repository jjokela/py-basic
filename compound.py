# Compounding interest
# FV = PV * (1 + r)^t


def compound(present_value, interest_rate, time):
    return present_value * (1 + interest_rate) ** time

