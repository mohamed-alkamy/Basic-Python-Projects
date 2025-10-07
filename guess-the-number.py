import random

print("Number Guessing Game")
print("I'm thinking of a number between 1 and 100. (You have 10 attempts to guess it.)")

playing = True
while playing:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    game_over = False

    while attempts < max_attempts and not game_over:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            game_over = True
        
        if attempts < max_attempts and not game_over:
            print(f"You have {max_attempts - attempts} attempts left.")

    if not game_over:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.") 
    
    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if not play_again.startswith('y'):
        playing = False