from student import Student
def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student.to_csv() + "\n")

def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
          for line in file:
            student_id, name, age, marks = line.strip().split(",")
            students.append(Student(int(student_id), name, int(age), float(marks)))
    except FileNotFoundError:
        return students
    return students

