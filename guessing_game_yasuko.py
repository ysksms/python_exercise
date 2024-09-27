import random

# generate a random number
answer = random.randint(1, 1000)

# set initial range
min_limit = 1
max_limit = 1000
# the number of guesses
input_count = 0

while True:
    user_input = input(f"Enter your guess from {min_limit} to {max_limit}: ")

    # error handling for when the user enters a non-integer value.
    try:
        input_number = int(user_input)
    except ValueError:
        print("Invalid input! Please enter an integer value.")
        continue

    # check if the input number is within the specified range
    if input_number < min_limit or input_number > max_limit:
        print(f"Please enter a number within the range {min_limit} to {max_limit}.")
        continue

    # increment input count
    input_count += 1
    if input_number < answer:
        print(f"Wrong! Guess count: {input_count}")
        # update the minimum limit
        min_limit = input_number + 1
    elif input_number > answer:
        print(f"Wrong! Guess count: {input_count}")
        # update the maximum limit
        max_limit = input_number - 1
    else:
        print(f"You got it! The hidden number is {answer}")
        print(f"It took you {input_count} guess(es).")
        # end the game
        break
