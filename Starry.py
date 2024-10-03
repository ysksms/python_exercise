# Get the number of rows from the user
n = int(input("# rows: "))

# 1. Center-Aligned Pyramid Pattern
def pyramid(height):
    for i in range(1, height + 1):  # Loop through each row
        for j in range(height - i):  # Print spaces for centering the stars
            print(" ", end="")  # Print a space without a newline
        for j in range(2 * i - 1):  # Print stars for the current row
            print("*", end="")  # Print a star without a newline
        print()  # Move to the next line after printing the current row

# 2. Left-Aligned Triangle Pattern (Decreasing stars)
def left_triangle(height):
    for i in range(height, 0, -1):  # Loop through each row starting from `height` down to 1
        for j in range(i):  # Print `i` stars in the current row
            print("*", end="")  # Print a star without a newline
        print()  # Move to the next line after printing the current row

# 3. Centered arrow pattern with increasing and decreasing stars
def arrow_pattern(height):
    mid_point = (height // 2) + 1  # Calculate the middle point of the pattern

    # Upper part: Increase stars until mid_point
    for i in range(1, mid_point + 1):  # Loop from 1 to `mid_point`
        for j in range(i):  # Print stars equal to the row number
            print("*", end="")  # Print a star without newline
        print()  # Move to the next line after printing all stars in the current row

    # Lower part: Decrease stars from `mid_point - 1`
    for i in range(mid_point - 1, 0, -1):  # Loop from `mid_point - 1` to 1
        for j in range(i):  # Print stars equal to the row number
            print("*", end="")  # Print a star without newline
        print()  # Move to the next line after printing all stars in the current row

# 4. Hourglass Pattern
def hourglass(height):
    mid_point = (height // 2) + 1  # Calculate the middle point

    # Upper part of the hourglass (decreasing stars)
    for i in range(mid_point, 0, -1):  # Loop from `mid_point` down to 1
        for j in range(mid_point - i):  # Print leading spaces for centering
            print(" ", end="")  # Print a space without a newline
        for j in range(2 * i - 1):  # Print stars for the current row
            print("*", end="")  # Print a star without a newline
        print()  # Move to the next line after printing the current row

    # Lower part of the hourglass (increasing stars)
    for i in range(2, mid_point + 1):  # Loop from 2 up to `mid_point`
        for j in range(mid_point - i):  # Print leading spaces for centering
            print(" ", end="")  # Print a space without a newline
        for j in range(2 * i - 1):  # Print stars for the current row
            print("*", end="")  # Print a star without a newline
        print()  # Move to the next line after printing the current row

# 5. Diamond Pattern
def diamond(height):
    mid_point = (height // 2) + 1  # Calculate the middle point

    # Upper part of the diamond (increasing stars)
    for i in range(1, mid_point + 1):  # Start from 1 and increase to `mid_point`
        for j in range(mid_point - i):  # Print leading spaces for centering
            print(" ", end="")  # Print a space without a newline
        for j in range(2 * i - 1):  # Print stars for the current row
            print("*", end="")  # Print a star without a newline
        print()  # Move to the next line after printing the current row

    # Lower part of the diamond (decreasing stars)
    for i in range(mid_point - 1, 0, -1):  # Start from `mid_point - 1` and decrease to 1
        for j in range(mid_point - i):  # Print leading spaces for centering
            print(" ", end="")  # Print a space without a newline
        for j in range(2 * i - 1):  # Print stars for the current row
            print("*", end="")  # Print a star without a newline
        print()  # Move to the next line after printing the current row



# Display each pattern with the user-defined height

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
