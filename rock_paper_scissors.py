import random

while True:
    lists = ["Rock", "Paper", "scissors"]

    computer_selection = random.choice(lists)
    # print(f"Computer Selected: {computer_selection}")

    word = input("Enter a word to overpower computer choice: ").strip().capitalize()

    if not word:
        print("*" * 50)
        print("Error: Kindly enter a word ")
        print("*" * 50)
        continue

    if word not in lists:
        print("*" * 50)
        print("Invalid: Kindly enter a word that can be find within the list")
        print("*" * 50)
        continue

    if word == lists[0] and computer_selection == lists[2]:
        print("=" * 50)
        print(f"I WIN! - {lists[0]} crushies {lists[2]}")
        print("=" * 50)
    elif word == lists[1] and computer_selection == lists[0]:
        print("=" * 50)
        print(f"I WIN! - {lists[1]} covers {lists[0]}")
        print("=" * 50)
    elif word == lists[2] and computer_selection == lists[1]:
        print("=" * 50)
        print(f"I WIN! - {lists[2]} cuts {lists[1]}")
        print("=" * 50)
    else:
        print("=" * 50)
        print(f"We DRAW! - Computer selected {computer_selection}")
        print("=" * 50)

# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
    print("*" * 50)
    print("*" * 50)
    again = input("Do you want to try again - (y/n): ").strip().lower()

    if again != "y":
        print("*" * 30)
        print("Game Over!")
        print("*" * 30)
        break
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------