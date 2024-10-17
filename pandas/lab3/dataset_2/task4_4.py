import pandas as pd
import matplotlib.pyplot as plt

df_students = pd.read_csv("students_grades.csv")

# Task 4: Data Visualization
print(
    "-----Task 4: a box plot to show the distribution of grades for each subject-----"
)

# Create a box plot to show the distribution of grades for each subject
df_students[["Math", "Science", "English", "History", "Physical_Education"]].boxplot()
plt.title("Distribution of Grades for Each Subject")
plt.ylabel("Grades")
plt.show()
