def determine_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    else:
        return "F"


def main():
    name = input("Enter the student's name: ")
    score = float(input("Enter the student's score: "))

    grade = determine_grade(score)
    print("\n--- Student Report Card ---")
    print(f"Name:  {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
if __name__ == "__main__":
    main()