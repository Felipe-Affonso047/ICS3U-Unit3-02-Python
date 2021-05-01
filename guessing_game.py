#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program is a guessing number game

def main():
    print("Try to guess a number from 0 to 9:")

    number = int(input())

    if number == 5:
        print("\nCongratulations, guessed right!")

    if number != 5:
        print("\nSorry, guessed wrong!")

    print("\nDone.")


if __name__ == "__main__":
    main()
