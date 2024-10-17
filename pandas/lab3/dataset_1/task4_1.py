import pandas as pd
import matplotlib.pyplot as plt

df_employees = pd.read_csv("employee_data.csv")

print(
    "-----Task 4: Data Visualization: a bar plot showing the average salary for each department-----"
)
# Create a bar plot showing the average salary for each department
department_avg_salary = df_employees.groupby("Department")["Salary"].mean()
department_avg_salary.plot(kind="bar", title="Average Salary for Each Department")
plt.ylabel("Average Salary")
plt.show()
