print('Grade Calculator')
combined_scores = []

while True:
    score = input('What is your score or "done"')
    if score.lower() == 'done':
        print('Bye')
        break

    combined_scores.append(float(score))
    average = sum(combined_scores) / len(combined_scores)
    print(f'Average scores: {average:.1f}')

    if average >= 90:
        print('A')
    elif average >= 80:
        print('B')
    elif average >= 70:
        print('C')
    else:
        print('D or F')