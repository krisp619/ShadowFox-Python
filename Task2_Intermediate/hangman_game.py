import random

# Hangman visual stages
hangman_stages = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ===
    """,
]

def play_hangman():
    words = ["python", "internship", "superman", "laptop", "developer"]
    word_to_guess = random.choice(words)
    hidden_word = ["_"] * len(word_to_guess)
    guessed_letters = []
    lives = 6

    print("Welcome to Hangman Game!")
    print("Word to guess:", " ".join(hidden_word))

    while lives > 0 and "_" in hidden_word:
        print(hangman_stages[6 - lives])
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct guess!")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    hidden_word[i] = guess
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

        print("Current word:", " ".join(hidden_word))
        print("Guessed so far:", ", ".join(guessed_letters))
        print("-" * 30)

    if "_" not in hidden_word:
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print(hangman_stages[6])
        print("Game Over! The word was:", word_to_guess)

while True:
    play_hangman()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! Goodbye!")
        break


