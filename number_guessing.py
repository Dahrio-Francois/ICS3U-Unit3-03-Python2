#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets you play a number guessing game
#   with user input


import constants


def main():
    # this program starts the game

    integer = int(input("Enter your guess between 0 & 9: "))

    # process
    if integer == constants.number:
        # output
        print("\nCorrect! You guessed the right number!")
        print("\nDone")
        
    elif integer != constants.number:
        print("\nIncorrect! Try again?")
        print("\nDone")


if __name__ == "__main__":
    main()
