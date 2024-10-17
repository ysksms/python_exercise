import pandas as pd
import matplotlib.pyplot as plt

df_students = pd.read_csv("students_grades.csv")

# Task 4: Data Visualization
print("-----Task 4: a bar plot showing the average grade for each subject-----")
# Create a bar plot showing the average grade for each subject
subject_means = df_students[
    ["Math", "Science", "English", "History", "Physical_Education"]
].mean()
subject_means.plot(kind="bar", title="Average Grade for Each Subject")
plt.ylabel("Average Grade")
plt.show()
