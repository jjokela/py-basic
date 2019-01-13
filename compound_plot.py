import matplotlib.pyplot as plt
from compound import compound

# future value
# interest

present_value = 1000
rate = 0.05

# x-values - time
xTime = list(range(0, 11))

# y-value - FV
yValue = [compound(present_value, rate, x) for x in xTime]

plt.plot(xTime, yValue, label="FV")

plt.title("Compounding Interest")
plt.xlabel("Time")
plt.ylabel("Value")

plt.legend()
plt.show()


