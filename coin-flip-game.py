import random

print('Coin flip game')

while True:
    guess = input('\nGuess heads or tails: ').lower()

    if guess != "heads" and guess != "tails":
        print('Invalid input')
        continue

    flip = random.choice(['heads', 'tails'])

    print(f'\n Coin shows {flip}')

    if guess == flip:
        print('Right guess')
    else:
        print('Right guess')

    again = input('\n Wanna play again? (y/n): ').lower()

    if not again.startswith('y'):
        print('Bye')
        break