from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
           raise TypeError("Only Student objects can be added.")
        if self.search_student(student.student_id):
            raise ValueError(f"Student with ID {student.student_id} already exists.")
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            student.display()

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False
    
    def update_student(self, student_id, name=None, age=None, marks=None):
        student = self.search_student(student_id)
        if student:
            if name is not None:
                student.name = name
            if age is not None:
                student.age = age
            if marks is not None:
                student.marks = marks
            return True
        return False

