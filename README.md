# CodeAlpha_hangmanGame
A  text-based Hangman game built in Python as part of the CodeAlpha Python Programming Internship.

📌 Goal	

A simple text-based Hangman game where the player guesses a word one letter at a time, built as part of the **CodeAlpha Python Programming Internship**.

  📁 Project Files

| File | Purpose |
|------|---------|
| `hangman.py` | Main script — the Hangman game |

 

  ▶ How to Run

Uses only built-in Python modules — no installation needed.

```
python hangman.py
```

 🎮 How to Use

1. The game randomly picks a word from a predefined list.
2. The word is shown as underscores (`_`), one for each letter.
3. Guess one letter at a time.
4. Correct guesses reveal the letter's position(s) in the word.
5. Incorrect guesses count toward your **6 allowed wrong guesses**.
6. Guess the whole word before running out of guesses to win!
7. After the game ends, you can choose to play again.

🔍 Sample Output

```
========================================
Welcome to Hangman!
You have 6 wrong guesses allowed.
========================================

Word: _ _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: None
Guess a letter: p
Good guess! 'p' is in the word.

Word: p _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: p
Guess a letter: z
Wrong guess! 'z' is not in the word.
```

  💡 Key Concepts Used

- **random** — picking a random word from the list
- **while loop** — keeping the game running until win/loss
- **if-else** — checking correct/incorrect guesses
- **strings** — building the word display
- **lists** — storing the word bank and guessed letters

---

  👤 Author

Arisha Khan
CodeAlpha Python Programming Intern

