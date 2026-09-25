questions = [
    ("What is the capital of Japan?", { "A" : "Beijing", "B" : "Seoul", "C" : "Tokyo", "D" : "Bangkok"}, "C")
    ("Which country has the largest total land area?", { "A" : "Canada", "B" : "Russia", "C" : "China", "D" : "United States"}, "B")
    ("Which country is known as the Land of the Rising Sun?", { "A" : "Japan", "B" : "Thailand", "C" : "South Korea", "D" : "Vietnam"}, "A")
    ("What is the capital of Japan", { "A" : "Beijing", "B" : "Seoul", "C" : "Tokyo", "D" : "Bangkok"}, "C")
    ("What is the capital of Japan", { "A" : "Beijing", "B" : "Seoul", "C" : "Tokyo", "D" : "Bangkok"}, "C")
]

while True:
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