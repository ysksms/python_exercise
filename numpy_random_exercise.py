import numpy as np

# Task 1: Creating a 1D NumPy Array
print("-----Task 1-----")
# create an array with numbers from 1 to 30
array_1d = np.arange(1, 31)
print("* 1D Array:")
print(array_1d)
print(f"* Shape of array: {array_1d.shape}")
print(f"* Element at index 10: {array_1d[10]}")
print()  # add an empty line at the end to separate output for better clarity

# Task 2: Creating a 2D NumPy Array
print("-----Task 2-----")
array_2d = array_1d.reshape(6, 5)
# reshape the 1D array into a 2D array of shape (6, 5)
print("* 2D Array:")
print(array_2d)
print(f"* Element at row 3, column 4: {array_2d[2, 3]}")
print()

# Task 3: Subsetting a 2D Array
print("-----Task 3-----")
print("* Third row of the 2D array:")
# extract and print the third row
print(array_2d[2, :])
print("* First two rows and last three columns:")
print(array_2d[:2, -3:])
print()

# Task 4: Generating Random Integer Array
print("-----Task 4-----")
# generate a 1D array of 15 random integers between 10 and 100
random_array_1d = np.random.randint(10, 101, 15)
print("* 1D Random Integer Array:")
print(random_array_1d)
print(f"* Maximum value: {random_array_1d.max()}")
print(f"* Minimum value: {random_array_1d.min()}")
print()

# Task 5: Generating a 2D Random Array
print("-----Task 5-----")
# generate a 2D array of shape (4, 4) with random integers between 0 and 50
random_array_2d = np.random.randint(0, 51, (4, 4))
print("* 2D Random Array:")
print(random_array_2d)
print(f"* Sum of all elements: {random_array_2d.sum()}")
print()

# Task 6: Manipulating Arrays
print("-----Task 6-----")
# shape (5, 5)
manipulated_array = np.random.randint(1, 21, (5, 5))
print("* Original Array:")
print(manipulated_array)
# set second row to 0
manipulated_array[1, :] = 0
print("* Array after setting second row to 0:")
print(manipulated_array)

# replace all values greater than 10 with 99
manipulated_array[manipulated_array > 10] = 99
print("* Array after replacing all values greater than 10 with 99:")
print(manipulated_array)
print()

# Task 7: Arithmetic Operations on Arrays
print("-----Task 7-----")
# create two 1D arrays of length 5 with random integers between 1 and 10
array_a = np.random.randint(1, 11, 5)
array_b = np.random.randint(1, 11, 5)
print("* Array A:")
print(array_a)
print("* Array B:")
print(array_b)
print(f"* Addition of A and B: {array_a + array_b}")
print(f"Subtraction of A and B: {array_a - array_b}")
print(f"Multiplication of A and B: {array_a * array_b}")
print()

# Task 8: Broadcasting in NumPy
print("-----Task 8-----")
# create a 1D array of length 4 with values [2, 4, 6, 8]
array_c = np.array([2, 4, 6, 8])
# create a 2D array of shape (3, 4) with random integers between 1 and 5
array_d = np.random.randint(1, 6, (3, 4))
print("* 1D Array C:")
print(array_c)
print("* 2D Array D:")
print(array_d)
print("* Adding C to each row of D:")
print(array_d + array_c)
print()

# Task 9: Filtering an Array
print("-----Task 9-----")
# generate a 1D array of 20 random integers between 1 and 100
filter_array = np.random.randint(1, 101, 20)
print("* Original Array:")
print(filter_array)
print("* Elements greater than 50:")
print(filter_array[filter_array > 50])
print("* Array with values less than 30 replaced with -1:")
filter_array[filter_array < 30] = -1
print(filter_array)
print()

# Task 10: Reshaping Arrays
print("-----Task 10-----")
# generate a 1D array of 12 random integers between 1 and 50
reshape_array = np.random.randint(1, 51, 12)
print("* Original 1D Array:")
print(reshape_array)
# reshape the array into a 3x4 2D array
reshape_array_2d = reshape_array.reshape(3, 4)
print("* Reshaped 2D Array:")
print(reshape_array_2d)
# transpose the array
transpose_array = np.transpose(reshape_array_2d)
print("* Transposed Array:")
print(transpose_array)
