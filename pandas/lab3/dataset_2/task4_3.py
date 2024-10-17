import pandas as pd
import matplotlib.pyplot as plt

df_students = pd.read_csv("students_grades.csv")

# Task 4: Data Visualization
print("-----Task 4: a histogram showing the distribution of Math scores-----")

# Create a histogram showing the distribution of Math scores
df_students["Math"].plot(
    kind="hist", bins=10, edgecolor="black", title="Distribution of Math Scores"
)
plt.xlabel("Math Scores")
plt.show()
