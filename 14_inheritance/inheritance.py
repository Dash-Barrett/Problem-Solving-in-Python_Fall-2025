class Student:
    def __init__(self, name, student_id, major):
        self.__name = name
        self.__student_id = student_id
        self.__major = major
    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__student_id}, Major: {self.__major}"
    
    def getName(self):
        print(self.__name)

class UndergraduateStudent(Student):
    # Overriding methods
    def __init__(self, name, student_id, major, year):
        super().__init__(name, student_id, major)
        self.__year = year
    
    def __str__(self):
        return super().__str__() + f", Year: {self.__year}"
    
    

if __name__ == "__main__":
    student = Student("Alice", "U1020", "Computer Science")
    print(student)
    
    undergrad = UndergraduateStudent("Michael", "U1222", "Physics", "Freshman")
    print(undergrad)
    undergrad.getName()