import random


word_bank = ["python", "coding", "vscode", "player", "gaming"]


secret_word = random.choice(word_bank)


guessed_word = ["_"] * len(secret_word)

incorrect_guesses_left = 6
guessed_letters = []  # Keeps track of all letters the player has already tried

print("--- Welcome to Text-Based Hangman! ---")


while incorrect_guesses_left > 0 and "_" in guessed_word:
    print("\n" + " ".join(guessed_word))
    print(f"Guesses remaining: {incorrect_guesses_left}")
    print(f"Letters guessed so far: {', '.join(guessed_letters)}")

    
    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input. Please enter a single letter.")
        continue

    
    if guess in guessed_letters:
        print(f"⚠️ You already guessed '{guess}'. Try a different letter!")
        continue

    
    guessed_letters.append(guess)

    
    if guess in secret_word:
        print(f"🎯 Good job! '{guess}' is in the word.")
        
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                guessed_word[index] = guess
    else:
        print(f"❌ Oops! '{guess}' is not in the word.")
        incorrect_guesses_left -= 1


print("\n" + "=" * 30)
if "_" not in guessed_word:
    print(f"🎉 Congratulations! You won! The word was: {secret_word}")
else:
    print(f"💀 Game Over! You ran out of guesses. The word was: {secret_word}")
print("=" * 30)