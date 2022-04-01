#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets you play a number guessing game
#   with user input


import random

some_variable = random.randint(0, 9)


def main():
    # this program starts the game

    integer = int(input("Enter your guess between 0 & 9: "))  # a number between 0 & 9

    # process
    if integer == some_variable:
        # output
        print("\nCorrect! You guessed the random number!")

    elif integer != some_variable:
        print("\nIncorrect!")
        print("The random number was {}.".format(some_variable))
        print("Try again?")

    print("\nDone")


if __name__ == "__main__":
    main()
