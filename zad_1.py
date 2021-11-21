class Student:
    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def isPassed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


student1 = Student('Jan Kowalski', 65)
student2 = Student('Andrzej Nowak', 45)