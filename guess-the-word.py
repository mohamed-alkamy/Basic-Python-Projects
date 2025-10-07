import random

print("Welcome to 'Guess the Word'!")
print("Unscramble the letters to form a valid word.")

words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift', 'go', 'rust']

while True:
    orginal_word = random.choice(words)

    letters = list(orginal_word)
    random.shuffle(letters)
    scrambled_word = ''.join(letters)

    print(f"\nScrambled word: {scrambled_word}")

    guess = input("Your guess: ").strip().lower()

    if guess == orginal_word:
        print("Correct! Well done.")
    else:
        print(f"Wrong! The correct word was '{orginal_word}'.")
    
    again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if not again.startswith('y'):
        break