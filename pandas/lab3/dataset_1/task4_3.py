import pandas as pd
import matplotlib.pyplot as plt

df_employees = pd.read_csv("employee_data.csv")

print(
    "-----Task 4: Data Visualization: a histogram showing the distribution of employee ages-----"
)

# Create a histogram showing the distribution of employee ages
df_employees["Age"].plot(
    kind="hist", bins=10, edgecolor="black", title="Distribution of Employee Ages"
)
plt.xlabel("Age")
plt.show()
