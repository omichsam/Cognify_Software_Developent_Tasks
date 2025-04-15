# Number Guessing Game

A simple text-based number guessing game implemented in Python.

## Description
This is a beginner-friendly Python program where the player tries to guess a randomly generated number between 1 and 10. The game provides feedback on whether the guess was too high or too low, and gives the player 3 attempts to guess correctly.

## Features
- Random number generation between 1-10
- 3 attempts to guess the number
- Immediate feedback on each guess
- Win/lose messages
- Simple and intuitive interface

## How to Run
1. Ensure you have Python 3 installed on your system
2. Download or copy the `number_guessing_game.py` file
3. Run the program using:
   ```bash
   python number_guessing_game.py
   ```

## Code 

    ``` bash
    import random

def number_guessing_game():
    target_number = random.randint(1, 10)
    attempts = 3
    
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 10. You have 3 attempts.")
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess == target_number:
            print("Congratulations! You guessed correctly!")
            return
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
    
    print(f"Game over! The correct number was {target_number}.")

number_guessing_game()

```

## How to Play
1. Run the program

2. Enter your guess when prompted

3. You'll get feedback if your guess was too high or too low

4. Try to guess the number within 3 attempts

## Possible Improvements
a. Add difficulty levels (different number ranges)

b. Keep track of high scores

c. Add a play-again option

d. Implement error handling for invalid inputs

## Author
Omichsam@gmail.com  || Michira Sam