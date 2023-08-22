import random
import time

def display_welcome():
    print("Welcome to GuessMaster: The Number Guessing Challenge!")
    print("Can you guess the secret number?\n")

def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (1-50 range, 10 attempts)")
    print("2. Medium (1-100 range, 7 attempts)")
    print("3. Hard (1-200 range, 5 attempts)")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        return 1, 50, 10
    elif choice == '2':
        return 1, 100, 7
    elif choice == '3':
        return 1, 200, 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 1, 100, 7

if __name__ == "__main__":
    pass