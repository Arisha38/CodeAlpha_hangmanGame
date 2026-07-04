"""
CodeAlpha Python Internship - Task 1
Hangman Game

A simple text-based Hangman game where the player guesses a word
one letter at a time.

Concepts used: random, while loop, if-else, strings, lists
"""

import random

# Predefined list of words to choose from
WORDS = ["python", "hangman", "internship", "developer", "codealpha"]

MAX_WRONG_GUESSES = 6


def choose_word():
    """Randomly pick a word from the WORDS list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses allowed.")
    print("=" * 40)

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            # Check if the player has won
            if all(letter in guessed_letters for letter in word):
                print("\n" + "=" * 40)
                print(f"Congratulations! You guessed the word: {word}")
                print("=" * 40)
                return
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    # Player has run out of guesses
    print("\n" + "=" * 40)
    print("Game Over! You've run out of guesses.")
    print(f"The word was: {word}")
    print("=" * 40)


if __name__ == "__main__":
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing! Goodbye.")
