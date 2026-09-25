import random

while True:
    names = input("Enter names: ").strip()

    if not names:
        print("*" * 50)
        print("Invaild: The input should not be empty")
        print("*" * 50)
        continue

    raw_names = names.split(",")

    if len(raw_names) == 1:
        print("*" * 50)
        print("Invaild: Enter more than a name")
        print("*" * 50)
        continue

    names_lists = []

    for name in raw_names:
        names_lists.append(name.strip().lower())

    # print(names_lists)

    secure_name = random.choice(names_lists)

    secure = []
    for _ in secure_name:
        secure.append("-")

    print("-" * 50)
    print("Guess each letter in the Secure name")
    print("-" * 20)
    print(f"Guess the letter: {" ".join(secure)}")
    print("-" * 50)

    lives = 6

    while lives > 0:
        guess = input("Guess the each letter of the secure name: ").strip().lower()

        if not guess:
            print("*" * 50)
            print("Empty: Enter a letter")
            print("*" * 50)
            continue

        if len(guess) != 1:
            print("*" * 50)
            print("Error: Enter just a letter")
            print("*" * 50)
            continue

        if not guess.isalpha():
            print("*" * 50)
            print("Invaild: Enter a letter not a number")
            print("*" * 50)
            continue

        if guess in secure_name:
            for index in range(len(secure)):
                if secure_name[index] == guess:
                    secure[index] = guess

            print(f"Correct!: {" ".join(secure)}")

        else:
            lives -= 1
            print("*" * 50)
            print(f"You have {lives} lives more.")
            print("-" * 20)
            print(f"Correct!: {" ".join(secure)}")
            print("-" * 20)
            continue


        if "-" not in secure:
            print("=" * 50)
            print("Congratulations! - You win")
            break

    if lives == 0:
        print("=" * 50)
        print("=" * 50)
        print("Game Over")
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