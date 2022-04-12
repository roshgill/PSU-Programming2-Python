class Course:
    def __init__(self, course):
        self.__courseName = course
        self.__students = []
        
    def addStudent(self, student):
        self.__students.append(student)
        
    def dropStudent(self, student):
        try:
            self.__students.remove(student)
        except:
            return
        
    def getStudents(self):
        students_list = self.__students
        return(students_list)
            
    def getNumber_of_students(self):
        num = len(self.__students)
        return num

    def getcourseName(self):
        name = self.__courseName
        return (name)