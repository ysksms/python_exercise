import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Basic DataFrame Operations
print("-----Task 1: Basic DataFrame Operations-----")
# Load the dataset into a Pandas DataFrame
df_students = pd.read_csv("students_grades.csv")

# Display the first 5 rows of the DataFrame
print("* First 5 rows of the DataFrame:")
print(df_students.head())

# Display the summary statistics of the DataFrame
print("\n* Summary statistics of the DataFrame:")
print(df_students.describe())

# Display the column names of the DataFrame
print("\n* Column names:")
print(df_students.columns)

# Count the number of male and female students
print("\n* Number of male and female students:")
print(df_students["Gender"].value_counts())
print()

# Task 2: Filtering and Subsetting
print("-----Task 2: Filtering and Subsetting-----")
# Filter the DataFrame to show only students who are 16 years old
print("* Students who are 16 years old:")
print(df_students[df_students["Age"] == 16])

# Filter the DataFrame to show only female students
print("\n* Female students:")
print(df_students[df_students["Gender"] == "F"])

# Filter the DataFrame to show students with Math scores above 85
print("\n* Students with Math scores above 85:")
print(df_students[df_students["Math"] > 85])

# Select the Name and Total_Grades columns for all students
df_students["Total_Grades"] = df_students[
    ["Math", "Science", "English", "History", "Physical_Education"]
].sum(axis=1)
print("\n* Name and Total_Grades columns:")
print(df_students[["Name", "Total_Grades"]])
print()

# Task 3: Aggregation and Grouping
print("-----Task 3: Aggregation and Grouping-----")

# 1. Calculate the average grade for each subject
print("* Average grade for each subject:")
print(
    df_students[["Math", "Science", "English", "History", "Physical_Education"]].mean()
)

# 2. Calculate the average grade for each gender (numeric columns only)
print("\n* Average grade for each gender:")
numeric_columns = ["Math", "Science", "English", "History", "Physical_Education"]
print(df_students.groupby("Gender")[numeric_columns].mean())

# 3. Calculate the total grades for each student (sum of all subjects)
df_students["Total_Grades"] = df_students[numeric_columns].sum(axis=1)

# Display the total grades for each student
print("\n* Total grades for each student:")
print(df_students[["Name", "Total_Grades"]])

# 4. Find the student with the highest total grade
print("\n* Student with the highest total grade:")
print(df_students[df_students["Total_Grades"] == df_students["Total_Grades"].max()])

# 5. Calculate the average age of the students
print("\n* Average age of the students:")
print(df_students["Age"].mean())
print()
