import random

while True:

    computer_picks = random.randint(1, 100)
    attempts = 5

    print("-" * 50)
    print("Computer have picked a number between 1 and 100. Try to guess it!")
    print("-" * 50)

    while attempts > 0:

        try:
            guess = int(input("Guess a number: ").strip())
        except ValueError:
            print("*" * 50)
            print("Invalid: Kindly enter number only")
            print("*" * 50)
            continue
        
        if guess > computer_picks:
            attempts -= 1
            print("=" * 50)
            print(f"You have {attempts} times to try again")
            print("High! - Try again!")
            print("=" * 50)
            continue
    
        elif guess < computer_picks:
            attempts -= 1
            print("=" * 50)
            print(f"You have {attempts} times to try again")
            print("Low! - Try again!")
            print("=" * 50)
            continue

        else:
            print("=" * 50)
            print("Congratulations! - You win!")
            print("=" * 50)
            break

    if attempts == 0:
        print("=" * 50)
        print("=" * 50)
        print("Game Over!")
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