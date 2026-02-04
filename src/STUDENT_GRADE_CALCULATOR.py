# src/STUDENT_GRADE_CALCULATOR.py

def calculate_average(marks):
    """Calculate average from a list of marks"""
    if not marks or len(marks) != 5:
        raise ValueError("Exactly 5 marks are required")
    return sum(marks) / len(marks)

def determine_grade(average):
    """Determine grade based on average marks"""
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"

def main():
    print("=== Student Grade Calculator ===")
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = calculate_average(marks)
    grade = determine_grade(average)
    print(f"\nAverage Marks: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
