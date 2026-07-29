class Student:
    def __init__(self,
                  student_id: int,
                    name: str,
                    age: int,
                    marks: float
                ):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def to_csv(self):
        return f"{self.student_id},{self.name},{self.age},{self.marks}"
