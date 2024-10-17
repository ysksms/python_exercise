import pandas as pd
import matplotlib.pyplot as plt

df_employees = pd.read_csv("employee_data.csv")

print(
    "-----Task 4: Data Visualization: a bar plot showing the total years at the company for each employee-----"
)

# Create a bar plot showing the total years at the company for each employee
df_employees = pd.read_csv("employee_data.csv")
df_employees.plot(
    x="Name",
    y="YearsAtCompany",
    kind="bar",
    title="Total Years at the Company for Each Employee",
)
plt.ylabel("Years at Company")
plt.show()
