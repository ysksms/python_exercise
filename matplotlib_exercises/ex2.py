# -----Exercise 2: Customizing Plots-----
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

plt.plot(x, y, color="green", linestyle="--", marker="o")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Exercise 2: Customized Line Plot")
plt.grid(True)
plt.show()
