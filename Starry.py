# get the number of rows from the user
n = int(input("# rows: "))

# 1. Center-Aligned Pyramid Pattern
def pyramid(height):
    for i in range(1, height + 1):
        for j in range(height - i):  # print spaces for centering the stars
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()  # move to the next line after printing the current row

# 2. Left-Aligned Triangle Pattern (decreasing stars)
def left_triangle(height):
    for i in range(height, 0, -1):  # example of array  [7, 6, 5, 4, 3, 2, 1]
        for j in range(i):
            print("*", end="")
        print()  # move to the next line after printing the current row

# 3. Centered arrow pattern with increasing and decreasing stars
def arrow_pattern(height):
    mid_point = (height // 2) + 1  # calculate the middle point of the pattern

    # upper part: increase stars until mid_point
    for i in range(1, mid_point + 1):  # example of array  [1, 2, 3, 4]
        for j in range(i):  # print stars equal to the row number
            print("*", end="")
        print()  # move to the next line after printing all stars in the current row

    # lower part: decrease stars from `mid_point - 1`
    for i in range(mid_point - 1, 0, -1):  # example of array  [3, 2, 1]
        for j in range(i):  # print stars equal to the row number
            print("*", end="")
        print()  # move to the next line after printing all stars in the current row

# 4. Hourglass Pattern
def hourglass(height):
    mid_point = (height // 2) + 1  # calculate the middle point

    # upper part of the hourglass (decreasing stars)
    for i in range(mid_point, 0, -1):  # example of array  [4, 3, 2, 1]
        for j in range(mid_point - i):  # print leading spaces for centering
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()  # move to the next line after printing the current row

    # lower part of the hourglass (increasing stars)
    for i in range(2, mid_point + 1):  # example of array  [2, 3, 4]
        for j in range(mid_point - i):  # print leading spaces for centering
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()  # move to the next line after printing the current row

# 5. Diamond Pattern
def diamond(height):
    mid_point = (height // 2) + 1  # calculate the middle point

    # Upper part of the diamond (increasing stars)
    for i in range(1, mid_point + 1):  # example of array  [1, 2, 3, 4]
        for j in range(mid_point - i):  # print leading spaces for centering
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()  # move to the next line after printing the current row

    # lower part of the diamond (decreasing stars)
    for i in range(mid_point - 1, 0, -1):  # example of array  [3, 2, 1]
        for j in range(mid_point - i):  # print leading spaces for centering
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()  # move to the next line after printing the current row


# display each pattern with the user-defined height

print("1. Center-Aligned Pyramid Pattern")
pyramid(n)

print("\n2. Left-Aligned Triangle Pattern")
left_triangle(n)

print("\n3. Right-Aligned Triangle Pattern")
arrow_pattern(n)

print("\n4. Hourglass Pattern")
hourglass(n)

print("\n5. Diamond Pattern")
diamond(n)

# references
# https://www.idtech.com/blog/what-is-n-in-python
# https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
# https://www.toppr.com/guides/python-guide/references/methods-and-functions/python-range/
# https://stackoverflow.com/questions/9910090/python-range-with-negative-strides