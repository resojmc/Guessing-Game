# Imports random module
import random

# Assigns a random int to number
number = random.randint(0, 10)
# Represents number of lives
status = 3
# Prints the title of the game
print(""" 
               - Jmc's -             v 1.0
            *Guessing Game*               
""")
# A loop that ask's the user to guess a number between 1 and 10
while status != 0:
    guess = input("Guess a number from 0 - 10: ")
    guess = int(guess)
    if guess == number:
        print(f"{number} is the number! Well Done!")
        break
 
    elif guess != number and guess < 11 and guess > -1:
        if status != 1 and status != 2:
            status = status - 1
            print(f"Wrong. {status} tries left. Try Again.")
        
        elif status == 2:
            status = status - 1
            print(f"Wrong. {status} try left. Try Again.")

        elif status == 1:
            print(f"You Failed. The number was {number}.")
            break
    # If the number the user provides is > 10 or < 0, Program does not count it as an attempt
    elif guess > 10 or guess < 0:
        if status != 0:
            print(f"{guess}... Invalid Answer. Try Again.")
