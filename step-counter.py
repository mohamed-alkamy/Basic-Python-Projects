print('Step counter')
daily_goal = int(input('\nWhat is your daily step goal? '))
current_steps = int(input('\nHow many steps have you taken today? '))
remaining = daily_goal - current_steps

if remaining > 0:
    print(f'You have {remaining} step(s) remaining.')
else:
    print(f'You have exceeded your goal by {-remaining} step(s).')