def calculate_average(scores):
    if len(scores) == 0:
        return 0.0

    return round(sum(scores) / len(scores), 2)


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def add_student(students):
    name = input("Student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    student_id = int(input("Student ID: "))

    if find_student(students, student_id) is not None:
        print(f"Student ID {student_id} already exists.")
        return

    number_of_scores = int(input("How many scores? "))
    
    if number_of_scores <= 0:
            print("The number of scores must be greater than zero.")
            return

    scores = []

    for score_number in range(1, number_of_scores + 1):
        while True:
            score = float(input(f"Enter score {score_number}: "))
            
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Score must be between 0 and 100.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)

    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("\n" + "-" * 75)
    print(f"{'Name      '}{'ID      '}{'Scores      '}{'Average'}")
    print("-" * 75)

    for student in students:
        scores_text = ", ".join(str(score) for score in student["scores"])
        average = calculate_average(student["scores"])

        print(
            f"{student['name']}     "
            f"{student['id']}       "
            f"{scores_text}     "
            f"{average}"
        )

    print("-" * 75)


def calculate_student_average(students):
    student_id = int(input("Enter student ID: "))

    student = find_student(students, student_id)

    if student is None:
        print(f"No student was found with ID {student_id}.")
        return

    average = calculate_average(student["scores"])

    print(f"{student['name']}'s average score: {average:.2f}")


def display_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_all_students(students)

        elif choice == "3":
            calculate_student_average(students)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


main()