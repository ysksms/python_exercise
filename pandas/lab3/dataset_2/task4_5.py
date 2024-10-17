import pandas as pd
import matplotlib.pyplot as plt

df_students = pd.read_csv("students_grades.csv")

# Task 4: Data Visualization
print(
    "-----Task 4: a scatter plot showing the relationship between Math and Science scores-----"
)

# Create a scatter plot showing the relationship between Math and Science scores
plt.scatter(df_students["Math"], df_students["Science"])
plt.title("Relationship Between Math and Science Scores")
plt.xlabel("Math Scores")
plt.ylabel("Science Scores")
plt.show()
