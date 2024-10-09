# -----Exercise 10: Line Plot with Annotations-----
import matplotlib.pyplot as plt

x = range(0, 20)
y = [value**2 for value in x]

plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Exercise 10: Line Plot with Annotations")

lowest_value = min(y)
lowest_index = y.index(lowest_value)
plt.annotate(
    "Lowest Point",
    xy=(lowest_index, lowest_value),
    xytext=(lowest_index + 2, lowest_value + 50),
    arrowprops=dict(facecolor="blue", arrowstyle="->"),
)

highest_value = max(y)
highest_index = y.index(highest_value)
plt.annotate(
    "Highest Point",
    xy=(highest_index, highest_value),
    xytext=(highest_index - 4, highest_value - 50),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
)


plt.show()
