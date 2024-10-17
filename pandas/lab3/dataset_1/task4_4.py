import pandas as pd
import matplotlib.pyplot as plt

df_employees = pd.read_csv("employee_data.csv")

print(
    "-----Task 4: Data Visualization: a box plot to show the distribution of salaries for each department-----"
)

# Create a box plot to show the distribution of salaries for each department
df_employees[["Department", "Salary"]].boxplot(by="Department")
plt.title("Distribution of Salaries for Each Department")
plt.ylabel("Salary")
plt.show()
