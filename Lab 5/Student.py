class Student:
    def __init__(self, user):
        self.__username = user
        self.__courses = []
        
    def addCourse(self, course):
        self.__courses.append(course)

    def dropCourse(self, course):
        try:
            self.__courses.remove(course)
        except:
            print("This course is not in your current schedule")

    def getCourse(self):
        course_list = self.__courses
        return (course_list)
    
    def getUser(self):
        user = self.__username
        return(user)