from student import Student
from student_manager import StudentManager
import file_handler


def main():
    # Create StudentManager object
    student_manager = StudentManager()

    # Create sample students
    students = [
        Student(1, "Alice", 20, 85),
        Student(2, "Bob", 22, 90),
        Student(3, "Charlie", 21, 95),
        Student(4, "David", 23, 88),
    ]

    # Add students
    for student in students:
        student_manager.add_student(student)

    # Display all students
    student_manager.display_students()

    # Search for a student
    student = student_manager.search_student(3)

    if student:
        print("Student Found:")
        student.display()
    else:
        print("Student not found.")

    # Remove a student
    if student_manager.remove_student(2):
        print("Student removed successfully.")
    else:
        print("Student not found.")

    print("\nStudents after removal:")
    student_manager.display_students()

    # Update a student
    if student_manager.update_student(1, name="Farhan", age=22, marks=99):
        print("Student updated successfully.")
    else:
        print("Student not found.")

    print("\nStudents after update:")
    student_manager.display_students()

    # Save students to file
    file_handler.save_students(student_manager.students)
    print("\nStudents saved successfully!")

    # Load students from file
    loaded_students = file_handler.load_students()

    for student in loaded_students:
        student.display()


if __name__ == "__main__":
    main()
    
