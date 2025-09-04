import random

print('Random recipe generator')

proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies = ["broccoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs = ["rice", "pasta", "potatoes", "quinoa", "bread"]
methods = ["baked", "grilled", "stir-fried", "roasted", "sautéed"]
flavors = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]

while True:

    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carb)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(f'\n Your random recipe is {flavor} {method} with {protein} with {veggie} and {carb}')

    if not input('Wanna try again? (y/n): ').lower().startswith():
        print('Bye')
        break