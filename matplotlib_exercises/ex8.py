# -----Exercise 8: Stacked Bar Plot-----
import matplotlib.pyplot as plt
import numpy as np

categories = ["Group 1", "Group 2", "Group 3"]
value1 = [5, 7, 3]
value2 = [6, 8, 4]
value3 = [4, 3, 5]

plt.bar(categories, value1, label="Value 1")
plt.bar(categories, value2, bottom=value1, label="Value 2")
plt.bar(categories, value3, bottom=np.array(value1) + np.array(value2), label="Value 3")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Exercise 8: Stacked Bar Plot")
plt.legend()
plt.show()
