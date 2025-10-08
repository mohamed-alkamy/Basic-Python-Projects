import random
import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



print("Welcome to the Memory Sequence Game!")
print("Try to remember the sequence of numbers displayed.")
print("\nRules:")
print("Wacth the numbers appear one by one.")
print("After the sequence is shown, you will need to input the entire sequence.")
print("Each round adds one more number to the sequence.")
print("How far can you go?")

input("\nPress Enter to start the game...")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))

    clear_screen()
    print(f"Round {current_round}:")
    print(f"Remeber this sequence of {len(sequence)} numbers:")

    for number in sequence:
        time.sleep(0.7)
        print(f"\n{number}")
        time.sleep(0.7)
        clear_screen()
    
    print("\nNow repeat the seuqnce by typing each number, separatred by spaces: ")
    player_answer = input("> ")

    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        game_over = True
        continue

    if player_sequence == sequence:
        print("Correct! Get ready for the next round.")
        current_round += 1
        time.sleep(2)
    else:
        print(f"Game over! You remevbered {current_round - 1} round(s) correctly.")
        print(f"The correct sequence was: {"".join(str(num) for num in sequence)}")
        game_over = True

    if game_over:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'y']:
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for playing! Goodbye.")