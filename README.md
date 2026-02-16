Here's a sample README file for your Bingo game:

---

# Bingo Game - Number Guessing Game

## Overview

This is a simple Python-based number guessing game where the user has to guess a randomly generated number within a certain range. The player has 3 attempts to guess the correct number. If they fail to guess the number correctly within the given number of attempts, the game will notify them of the failure.

## Features

- Generates a random number between a specified range (1 to 10).
- Prompts the user to guess the number with a maximum of 3 attempts.
- Provides feedback after each guess, indicating whether the guess was correct or not.
- Displays the number of remaining attempts.
- Handles invalid inputs gracefully by notifying the user if they entered something that is not a valid number.

## Requirements

- Python 3.x

## How to Play

1. When you run the game, a random number between 1 and 10 will be generated.
2. You will be prompted to guess the number.
3. You have 3 attempts to guess the correct number.
4. If you guess the correct number, you win and the game ends.
5. If you run out of attempts without guessing correctly, the game ends and you will be informed that you failed to guess the number.

## Code Walkthrough

1. **generate_random_number()**:
   - This function generates a random number between 1 and 10 (inclusive).

2. **get_user_input()**:
   - This function prompts the user to input a number.
   - It includes error handling to ensure that the input is a valid integer. If the user enters an invalid number (e.g., a letter or special character), it will notify them and prompt for input again.

3. **check_guess_number()**:
   - This function checks if the user's input matches the randomly generated number.

4. **Main Game Loop**:
   - The main loop keeps track of the remaining guesses and calls the above functions to get input, check if the guess is correct, and provide feedback. The loop continues until the user either guesses correctly or runs out of attempts.

## Sample Output

```
== Your number should between 1 - 10 ==
Guess Number: 5
guess left: 2
Guess Number: 7
guess left: 1
Guess Number: 8
you couldn't guess number, and ran out of guesses!
```

## License

This project is open source and available under the [MIT License](LICENSE).