import pandas as pd
import matplotlib.pyplot as plt

df_students = pd.read_csv("students_grades.csv")

numeric_columns = ["Math", "Science", "English", "History", "Physical_Education"]
df_students["Total_Grades"] = df_students[numeric_columns].sum(axis=1)


# Task 4: Data Visualization
print("-----Task 4: a bar plot showing the total grades of each student-----")

# Create a bar plot showing the total grades of each student
df_students.plot(
    x="Name", y="Total_Grades", kind="bar", title="Total Grades of Each Student"
)
plt.ylabel("Total Grades")
plt.show()
