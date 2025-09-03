print('Character type checker')
char = input('Enter a character here: ')

if char.isalpha():
    print('This is a letter')
elif char.isdigit():
    print('This is a number')
else:
    print('This is a special character.')