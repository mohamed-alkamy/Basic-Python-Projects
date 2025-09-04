print('Vowel counter')

while True:

    text = input("Write a work or ('quit')")

    if text.lower() == 'quit':
        print('Bye')
        break

    vowel_count = 0

    for letter in text.lower():
        if letter in ["a", "e", "i", "o", "u"]:
            vowel_count += 1

    print(f"This word has {vowel_count} vowels")
