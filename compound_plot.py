import matplotlib.pyplot as plt

from compound import compound_yearly_value_with_interest

# future value
# interest

present_value = 1000
rate = 0.1
time = 30

# x-values - time
xTime = list(range(0, time+1))

result = compound_yearly_value_with_interest(present_value, rate, time)
unzipped = list(zip(*result))

# y-value - FV
yValue = unzipped[0]

# y-value - interest paid
yInterestPaid = unzipped[1]

plt.plot(xTime, yValue, label="FV")
plt.plot(xTime, yInterestPaid, label="Interest Paid")

plt.title("Compounding Interest")
plt.xlabel("Time")
plt.ylabel("Value")

plt.legend()
plt.show()


