from random import randint
import time

def initialize():

    game_length = int(input("Game length (in seconds): "))
    max_int = int(input("Maximum digit to multiply (ex: 5, 12, 20): "))

    score = 0
    starting_time = time.time()

    return game_length, max_int, score, starting_time

def run_turn(max_int, score):

    x = randint(0, max_int)
    y = randint(0, max_int)

    answer = (input(f"{x}*{y} = "))
    
    return answer == x*y

def run_to_completion():

    print("\nMultiplication game: Choose your settings.\n")

    game_length, max_int, score, starting_time = initialize()

    print("\nMultiplication game: Go!\n")

    while time.time() < starting_time + game_length:
                
        if run_turn(max_int, score):
            score += 1
        else:
            print("\nYou lose!\n")
            exit()

    print(f"\nTimes up! Your final score is: {score}!\n")

run_to_completion()

"""

print(value="", sep="", end="")

- "sep", short for separation, dictates how much separation there is between the comma-separated values. Default value is " " (a single space).
- "end" dictates what happens after the print statement. Default value is "\n" (a new line).

Ex:

print('G', 'G', sep='', end="")
print("hi")

------------------------------------------------

Note: add stuff from ICS31/function_design_recipe.py (types, docstrings, asserts) to my python functions.

"""