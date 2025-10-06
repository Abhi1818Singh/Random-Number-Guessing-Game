import random

def number_guessing_game():
    print("Welcome to my Number Guessing Game by Abhishek Singh(Proud OSC Member)")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number_to_guess:
                print("low! Try again.")
            elif guess > number_to_guess:
                print("high! Try again.")
            else:
                print(f"Congratulations! You guessed correct number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()