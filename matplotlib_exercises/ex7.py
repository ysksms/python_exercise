# -----Exercise 7: Pie Chart-----
import matplotlib.pyplot as plt

categories = ["Marketing", "Development", "Sales", "Support"]
values = [20, 35, 25, 20]

plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.title("Exercise 7: Pie Chart")
plt.legend(categories, loc="center left", bbox_to_anchor=(1, 0.5), title="Departments")
plt.show()
