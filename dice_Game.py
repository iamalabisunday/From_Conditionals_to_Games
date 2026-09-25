import random

while True:
    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    if player > computer:
        print("=" * 50)
        print("Congratulations! - Player wins!")
        print("=" * 50)
    elif player < computer:
        print("=" * 50)
        print("Congratulations! - Computer wins!")
        print("=" * 50)
    else:
        print("=" * 50)
        print("Tie Draw!")

# ===== Final Section ==============================================
    print("-" * 50)
    print(f"The final - Computer: {computer}, Player: {player}")
    print("-" * 50)
    print("-" * 50)

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