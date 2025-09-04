import random

print('Reverse name generator')

while True:
    name = (input('Write down name here: '))

    if not name:
        break
    
    reverse_name = name[::-1]
    print(f'Your reversed name is: {reverse_name}')
    print(f'In a paralled universe, they would call you {reverse_name.title()}')

    answer = input('Try another name (y/n): ')
    if answer != 'y':
        break