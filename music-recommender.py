import random

print('Music Recommender')

genres = {
    'rock': ['Elvis Presley', 'Queen', 'AC/DC'],
    'pop': ['Ed Sheeran', 'ATC'],
    'hip-hop': ['Drake', 'The Weekend']
}

choice = input('What genres do you like (rock, hip-hop, pop): ')

if choice not in genres:
    print("I don't know that genre.")
else:
    print(f'Check out {random.choice(genres[choice])}')