import pandas as pd
import matplotlib.pyplot as plt

df_employees = pd.read_csv("employee_data.csv")

print(
    "-----Task 4: Data Visualization: a scatter plot showing the relationship between age and salary-----"
)

# Create a scatter plot showing the relationship between age and salary
plt.scatter(df_employees["Age"], df_employees["Salary"])
plt.title("Relationship Between Age and Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
