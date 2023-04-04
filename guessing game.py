import random

number = random.randint(0, 10)
status = 3

print(""" 
               - Jmc's -             v 1.0
            *Guessing Game*               
""")

while status != 0:
    guess = input("Guess a number from 0 - 10: ")
    guess = int(guess)
    if guess == number:
        print(f"{number} was the number! Well Done!")
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
    
    elif guess > 10 or guess < 0:
        if status != 0:
            print(f"{guess}... Invalid Answer. Try Again.")
