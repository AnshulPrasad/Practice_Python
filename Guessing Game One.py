"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

target = random.randint(1, 10)
counter = 0
while True:
    pred = input("Enter prediction: ")
    if pred == "exit":
        break
    else:
        pred = int(pred)
        counter += 1
    if pred == target:
        print(f"won in {counter} attempt!")
        break
    elif pred < target:
        print("increase the number.")
    else:
        print("decrease the number.")
