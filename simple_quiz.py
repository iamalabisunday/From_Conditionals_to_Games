import random

questions = [
    ("What is the capital of Japan?", {"A": "Beijing", "B": "Seoul", "C": "Tokyo", "D": "Bangkok"}, "C"),
    ("Which country has the largest total land area?", {"A": "Canada", "B": "Russia", "C": "China", "D": "United States"}, "B"),
    ("Which country is known as the Land of the Rising Sun?", {"A": "Japan", "B": "Thailand", "C": "South Korea", "D": "Vietnam"}, "A"),
    ("What is the smallest country in the world by area?", {"A": "Monaco", "B": "Vatican City", "C": "San Marino", "D": "Liechtenstein"}, "B"),
    ("Which country has the highest population in the world?", {"A": "China", "B": "India", "C": "Indonesia", "D": "United States"}, "B")
]

while True:
    question_text, options, correct_answer = random.choice(questions)

    print("=" * 50)
    print("Question")
    print("-" * 10)
    print(question_text)

    for key, value in options.items():
        print(f"({key}) {value}")

    print("-" * 10)
    print("Answer")

    while True:
        print("-" * 50)
        answer = input("Enter your answer: ").strip().upper()

        if not answer:
            print("*" * 50)
            print("Invalid: Kindly enter an option")
            continue

        if not answer.isalpha():
            print("*" * 50)
            print("Error: Only enter a valid alphabet")
            continue

        if len(answer) != 1:
            print("*" * 50)
            print("Invalid: Kindly enter a single option only")
            continue

        if answer not in ("A", "B", "C", "D"):
            print("*" * 50)
            print("Error: Option must be between A and D")
            continue

        if answer == correct_answer:
            print("=" * 50)
            print("Congratulations! You are correct!")
        else:
            print("=" * 50)
            print(f"Wrong! The correct answer was ({correct_answer}).")
        break

    print("*" * 50)
    again = input("Do you want to try again? (y/n): ").strip().lower()

    if again != "y":
        print("*" * 30)
        print("Game Over!")
        print("*" * 30)
        break