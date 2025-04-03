import random

while True:
    input("Press Enter to roll the dice...")
    print("Rolling the dice...")
    print("You rolled:", random.randint(1, 6))
    again = input("Do you want to roll again? (y/n): ").strip().lower()
    if again != 'y':
        break
print("Thanks for playing!")