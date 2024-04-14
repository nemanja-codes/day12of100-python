from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input. Please try again.")
        return choose_difficulty()

def check_guess(guess, number):
    if guess == number:
        print(f"You got it! The answer was {number}.")
        return True
    elif guess > number:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num_to_guess = random.randint(1, 100)

    attempts = choose_difficulty()
    end_game = False

    while attempts > 0 and not end_game:
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        guess = int(input("Make a guess: "))
        end_game = check_guess(guess, num_to_guess)
        if attempts > 0 and not end_game:
            print("Guess again.")

    if attempts == 0 and not end_game:
        print("You've run out of guesses, you lose.")


play_game()
