import json
import os

FILE_NAME = "students.json"


# Load student data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Save student data
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a new student
def add_student(students):
    roll_no = input("Enter Roll Number: ").strip()

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch: ").strip()
    year = input("Enter Year: ").strip()

    students[roll_no] = {
        "name": name,
        "branch": branch,
        "year": year,
        "attendance": []
    }

    save_data(students)
    print("Student added successfully!")


# Mark attendance
def mark_attendance(students):
    if not students:
        print("No students found!")
        return

    roll_no = input("Enter Roll Number: ").strip()

    if roll_no not in students:
        print("Student not found!")
        return

    date = input("Enter Date (DD-MM-YYYY): ").strip()

    # Prevent duplicate attendance
    for record in students[roll_no]["attendance"]:
        if record["date"] == date:
            print("Attendance already marked for this date!")
            return

    status = input("Enter attendance (P for Present / A for Absent): ").upper()

    if status not in ["P", "A"]:
        print("Invalid input! Enter P or A.")
        return

    students[roll_no]["attendance"].append({
        "date": date,
        "status": "Present" if status == "P" else "Absent"
    })

    save_data(students)
    print("Attendance marked successfully!")


# View attendance records
def view_records(students):
    if not students:
        print("No students found!")
        return

    roll_no = input("Enter Roll Number: ").strip()

    if roll_no not in students:
        print("Student not found!")
        return

    student = students[roll_no]
    attendance = student["attendance"]

    print("\n----- Student Details -----")
    print("Roll Number :", roll_no)
    print("Name        :", student["name"])
    print("Branch      :", student["branch"])
    print("Year        :", student["year"])

    print("\n----- Attendance Records -----")

    if not attendance:
        print("No attendance records found.")
        return

    present = 0

    for record in attendance:
        print(record["date"], ":", record["status"])
        if record["status"] == "Present":
            present += 1

    total = len(attendance)
    percentage = (present / total) * 100

    print("\nTotal Classes :", total)
    print("Present       :", present)
    print("Absent        :", total - present)
    print("Attendance %  :", round(percentage, 2), "%")


# View all students
def view_students(students):
    if not students:
        print("No students found!")
        return

    print("\n----- Student List -----")

    for roll_no, student in students.items():
        print(
            "Roll No:", roll_no,
            "| Name:", student["name"],
            "| Branch:", student["branch"],
            "| Year:", student["year"]
        )


# Main menu
def main():
    students = load_data()

    while True:
        print("\n====================================")
        print(" STUDENT ATTENDANCE MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Records")
        print("4. View All Students")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            mark_attendance(students)

        elif choice == "3":
            view_records(students)

        elif choice == "4":
            view_students(students)

        elif choice == "5":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()