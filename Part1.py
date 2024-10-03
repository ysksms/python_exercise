# get input from the user
number = int(input("Enter the number: "))
n = int(input("Enter the position (from right): "))

# use integer division and mod to find the nth digit from the right
nth_digit = (number // 10**(n-1)) % 10

# print the result
print(f"The {n}th digit (from the right) is: {nth_digit}")

# references
# https://medium.com/@alopezmartinez/extracting-digits-from-an-integer-in-python-a-step-by-step-guide-96c9ff98db37
# https://stackoverflow.com/questions/41321533/how-to-extract-digits-from-a-number-from-left-to-right
