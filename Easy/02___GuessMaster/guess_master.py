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

def play_game():
    secret_number = random.randint(start_range, end_range)
    attempts_left = max_attempts

    while attempts_left > 0:
        guess = int(input("\nEnter your guess: "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number}!")
            print(f"You used {max_attempts - attempts_left + 1} attempts.")
            break
        
        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    if attempts_left == 0:
        print(f"\nSorry, you've run out of attempts. The secret number was {secret_number}.")

def main():
    display_welcome()
    global start_range, end_range, max_attempts
    start_range, end_range, max_attempts = choose_difficulty()
    play_game()

if __name__ == "__main__":
    main()