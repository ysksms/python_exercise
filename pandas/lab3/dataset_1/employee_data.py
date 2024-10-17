import pandas as pd

# Task 1: Basic DataFrame Operations
print("-----Task 1: Basic DataFrame Operations-----")
# Load the dataset into a Pandas DataFrame
df_employees = pd.read_csv("employee_data.csv")

# Display the first 5 rows of the DataFrame
print("* First 5 rows of the DataFrame:")
print(df_employees.head())

# Display the summary statistics of the DataFrame
print("\n* Summary statistics of the DataFrame:")
print(df_employees.describe())

# Display the column names of the DataFrame
print("\n* Column names:")
print(df_employees.columns)

# Count the number of employees in each department
print("\n* Number of employees in each department:")
print(df_employees["Department"].value_counts())
print()

# Task 2: Filtering and Subsetting
print("-----Task 2: Filtering and Subsetting-----")
# Filter the DataFrame to show only employees who are older than 40
print("* Employees older than 40:")
print(df_employees[df_employees["Age"] > 40])

# Filter the DataFrame to show only employees in the 'IT' department
print("\n* Employees in the 'IT' department:")
print(df_employees[df_employees["Department"] == "IT"])

# Filter the DataFrame to show employees with a salary above 75000
print("\n* Employees with a salary above 75000:")
print(df_employees[df_employees["Salary"] > 75000])

# Select the Name and Salary columns for all employees
print("\n* Name and Salary columns:")
print(df_employees[["Name", "Salary"]])

# Calculate the average salary for each department
print("\n* Average salary for each department:")
print(df_employees.groupby("Department")["Salary"].mean())
print()

# Task 3: Aggregation and Grouping
print("-----Task 3: Aggregation and Grouping-----")
# Calculate the average salary of all employees
print("* Average salary of all employees:")
print(df_employees["Salary"].mean())

# Calculate the average age of employees in each department
print("\n* Average age of employees in each department:")
print(df_employees.groupby("Department")["Age"].mean())

# Calculate the total years worked at the company for all employees
print("\n* Total years worked at the company for all employees:")
print(df_employees["YearsAtCompany"].sum())

# Find the employee with the highest salary
print("\n* Employee with the highest salary:")
print(df_employees[df_employees["Salary"] == df_employees["Salary"].max()])

# Calculate the average years at the company for each department
print("\n* Average years at the company for each department:")
print(df_employees.groupby("Department")["YearsAtCompany"].mean())
print()
