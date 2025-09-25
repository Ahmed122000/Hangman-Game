
# Hangman Game

A simple command-line-based Hangman game written in Python.

## Assumptions

1. **Player 1** is allowed to enter only lowercase letters (no numbers or special symbols). Punctuation like commas or slashes will remain visible.
2. **Player 2** must guess using lowercase letters only.
3. **Player 2** has a maximum of 10 incorrect guesses before losing the game.
4. Only **one character** is allowed per turn.

## How to Play

- **Player 1**: Enter a word for **Player 2** to guess (lowercase letters only).
- **Player 2**: Guess the hidden word by entering one letter at a time.
- For each incorrect guess, a part of the hangman is drawn. After 10 incorrect guesses, the hangman will be fully drawn, and Player 2 will lose.
- Enter 'quit' to quit the game

## Game Rules

- Player 2 will win if they guess the entire word before running out of guesses.
- The score starts at 100 and decreases by 10 with every incorrect guess.
- Player 2 can only enter one letter per turn.
- Letters that have been guessed already will not affect the game if entered again.

## Terminal Display

For the best experience, open the terminal in full screen to view the hangman drawing properly.

## Requirements

- Python 3.x

## How to Run

1. Clone this repository.
2. Run the following command in your terminal:
   ```bash
   python hangman.py
   ```

## Sample Game Output

```plaintext
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
   _|____________

   Loser
```

Enjoy the game!
