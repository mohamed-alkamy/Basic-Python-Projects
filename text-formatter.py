print ('Text capitalizer')
text = input('\nEnter text here: ')
print('1. Uppercase')
print('2. Lowercase')
print('3. Title case')
print('4. Sentence case')

choice = input('\n Choose a format')

if choice == '1':
    print(text.upper())
elif choice == '2':
    print(text.lower())
elif choice == '3':
    print(text.title())
elif choice == '4':
    print(text.capitalize())