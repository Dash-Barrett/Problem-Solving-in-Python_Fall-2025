
class Course:
    """
    course_name (private)
    list of students (private)

    addStudent(self, Student), shouldn't enroll the same student twice

    getCourseName

    getStudents

    getNumberOfStudents

    dropStudent(self, student), should provide a message with a dropped student's name, should check if student is enrolled in the course

    __str__ info about the course

    """

    # Variables
    __course_name = str()
    __studentsList = []

    # Constructor
    def __init__(self, course_name):
        self.__course_name = course_name

    # Methods
    def addStudent(self, Student):
        if Student not in self.__studentsList:
            self.__studentsList.append(Student)
    
    def getCourseName(self):
        return self.__course_name
    
    def getStudents(self):
        return self.__studentsList
    
    def getNumberOfStudents(self):
        return len(self.__studentsList)
    
    def dropStudent(self, student):
        if student in self.__studentsList:
            print(f"{student} has been dropped from {self.__course_name}")
            self.__studentsList.remove(student)
    
    def __str__(self):
        return f"Course Name: {self.__course_name}, Number of Students: {self.getNumberOfStudents()}"
    


class InPersonCourse(Course):
    """
    private 
    room_number
    schedule
    max_seats

    Override addStudent method (check, are there avaiable seats?), print appropriate message
    
    Override __str__
    """
    # New Variables
    __room_number = str()
    __schedule = str()
    __max_seats = int()

    # New Constructor
    def __init__(self, course_name, room_number, schedule, max_seats):
        super().__init__(course_name)
        self.__room_number = room_number
        self.__schedule = schedule
        self.__max_seats = max_seats

    # Methods (Overriden)
    def addStudent(self, Student):
        if Student not in self.getStudents() and self.getNumberOfStudents() < self.__max_seats:
            print(f"{Student} has been added to the course, the course now has {self.getNumberOfStudents()} students.")
            return super().addStudent(Student)
        else:
            print(f"{Student} has not been added to the course.")
    
    def __str__(self):
        return super().__str__() + f", Room Number: {self.__room_number}, Schedule: {self.__schedule}, {self.getNumberOfStudents()}/{self.__max_seats} seats filled"



if __name__ == "__main__":
    compSci = Course("C++")
    compSci.addStudent("Timmy")
    print(compSci)
    compSci.dropStudent("Timmy")
    print(compSci)
    
    compSci2 = InPersonCourse("Python", "IST 1032", "11:00am - 11:50am", 2)
    compSci2.addStudent("Timmy")
    compSci2.addStudent("Timmy")
    compSci2.addStudent("Alice")
    compSci2.addStudent("Luke")
    print(compSci2)