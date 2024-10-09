# -----Exercise 9: Box Plot-----
import matplotlib.pyplot as plt
import numpy as np

dataset1 = np.random.normal(60, 10, 100)
dataset2 = np.random.normal(70, 15, 100)
dataset3 = np.random.normal(80, 5, 100)

plt.boxplot(
    [dataset1, dataset2, dataset3], labels=["Dataset 1", "Dataset 2", "Dataset 3"]
)
plt.title("Exercise 9: Box Plot")
plt.show()
