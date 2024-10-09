# -----Exercise 5: Scatter Plot-----
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)  # 50 random x-values between 0 and 1
y = np.random.rand(50)  # 50 random y-values between 0 and 1

plt.scatter(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Exercise 5: Scatter Plot")
plt.show()
