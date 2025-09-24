"""Number guesser"""

import random

top_of_range = input("Type a number: ")  # top_of_range is a string now.

if top_of_range.isdigit():  # check if all characters in the string are digits.
    top_of_range = int(top_of_range)   # convert to an integer

else:
    print("Please type an positive integer number next time.")
    quit()


# r = random.randrange(-1, 10)  # not include 10
random_num = random.randint(0, top_of_range) # Return random integer in range [a, b], including both end points.
guess_time = 0

while True:
    guess_time += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_num:
        print("You got it!")
        break             # break out of the loop once you got it.
    elif user_guess > random_num:
        print("You were above the number.")
    else:
        print("You were below the number.")

print(f"You got it in {guess_time} guesses.")
