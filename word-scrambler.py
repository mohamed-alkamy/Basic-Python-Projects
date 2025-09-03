import random

print('Word Scrambler')

while True:
    word = input('Write the word to scramble or "done": ')
    if word.lower() == 'done':
        print('Bye')
        break

    letters = list(word)
    random.shuffle(letters)
    print(f'Scrambled: { "" .join(letters)}')