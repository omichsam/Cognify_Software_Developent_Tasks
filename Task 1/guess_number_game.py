# Import the random module to generate a random number
import random

def number_guessing_game():
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)
    # Set the number of attempts allowed
    attempts = 3
    
    # Display game instructions
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 10. You have 3 attempts.")
    
    # Looping for each attempt
    for attempt in range(1, attempts + 1):
        # Get the player's guess (convert input to integer)
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        # Checking if the guess is correct
        if guess == target_number:
            print("Congratulations! You guessed correctly!")
            return  # Exit the function if correct
        # Provides hints if the guess is wrong
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
    
    # Prints If all attempts are used without guessing correctly
    print(f"Game over! The correct number was {target_number}.")

# Run the game
number_guessing_game()