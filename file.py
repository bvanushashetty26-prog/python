
from login import login
from student_registration import register_student
from marks import collect_marks


def main():
    if not login():
        return

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Student Registration")
        print("2. Collect Student Marks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            collect_marks()
        elif choice == "3":
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
