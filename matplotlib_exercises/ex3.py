# -----Exercise 3: Bar Plot-----
import matplotlib.pyplot as plt

categories = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
values = [10, 15, 7, 12, 5]

plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Exercise 3: Bar Plot")
plt.show()
