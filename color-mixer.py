print ("Color Mixer")

color_mixes = {
    ('red', 'blue'): 'purple',
    ('red', 'yellow'): 'orange',
    ('blue', 'yellow'): 'green',
}

while True:
    color1 = input("\nEnter the first color (red, blue, yellow): ").strip().lower()
    color2 = input("Enter second color: ").strip().lower()

    mix = None

    if (color1, color2) in color_mixes:
        mix = color_mixes[(color1, color2)]
    elif (color2, color1) in color_mixes:
        mix = color_mixes[(color2, color1)]
    
    if mix:
        print(f"{color1} + {color2} = {mix}")
    else:
        print(f"Sorry, I don't know how to mix {color1} and {color2}.")

    if not input("\nMix more colors? (y/n): ").strip().lower().startswith('y'):
        break