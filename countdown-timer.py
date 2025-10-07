import time

print("Countdown Timer")
print("Count down from a specified number of seconds.")

while True:
    try:
        seconds = int(input("Enter the number of seconds to count down from: "))

        if seconds <= 0:
            print("Please enter a positive integer.")
            continue

        print(f"Counting down from {seconds} seconds...")

        for i in range(seconds, 0, -1):
            print(f"{i} seconds remaining", end='\r')
            time.sleep(1)

        print("\n Countdown finished!")

        again = input("Do you want to start another countdown? (yes/no): ").strip().lower()
        if not again.startswith('y'):
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")