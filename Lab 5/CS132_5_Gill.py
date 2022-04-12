from Student import Student
from Course import Course

LOOP = True
USERNAME_LIST = []
PASSWORD_LIST = []
CURRENT_STUDENT = ''

STUDENTS = []
COURSES = []

def save_courses_data():
    with open("CI.txt", 'w') as opened_file:
        opened_file.write("COURSES,STUDENTS\n")
        for course in COURSES:
            opened_file.write(f"{course.getcourseName()}")
            students_list = course.getStudents()
            students_len = len(students_list)
            
            if students_len < 1:
                opened_file.write("\n")
                continue
            
            for student in students_list:
                opened_file.write(",")
                opened_file.write(f"{student}")
                if student == students_list[students_len-1]:
                    opened_file.write("\n")
                    continue

def save_student_data():
    with open("SI.txt", 'w') as opened_file:
        opened_file.write("USERNAME,COURSES\n")
        for student in STUDENTS:
            opened_file.write(f"{student.getUser()}")
            course_list = student.getCourse()
            courses_num = len(course_list)
            
            if courses_num < 1:
                opened_file.write("\n")
                continue
            
            for course in course_list:
                opened_file.write(",")
                opened_file.write(f"{course}")
                if course == course_list[courses_num-1]:
                    opened_file.write("\n")
                    continue

def show_courses(current_user):
    list = current_user.getCourse()
    print("You are enrolled in:")
    for classes in list:
        print(classes)

def drop_course(current_user):
    course = str(input("Please enter which course you would like to drop: "))
    current_user.dropCourse(course)
    for course_check in COURSES:
        if course == course_check.getcourseName():
            course_check.dropStudent(current_user.getUser())

def add_course(current_user):
    courses = ['CS131','CS132','EE210','EE310','Math320','Math220']
    while True:
        course = str(input("Please enter which course you would like to add: "))
        if course not in courses:
            print("Please enter a valid course")
            continue
        else:
            current_user.addCourse(course)
            print("Course added")
            for course_check in COURSES:
                if course == course_check.getcourseName():
                    course_check.addStudent(current_user.getUser())
                    return

def available_courses():
    for course in COURSES:
        print(f"{course.getcourseName()} students number:{course.getNumber_of_students()}")

def manage_schedule(current_user):
    user_input = str(input("""A: Show all courses available\nB: Add a course\nC: Drop a course\nD: Show all my courses\nE: Exit\n:"""))
    if user_input == 'A':
        available_courses()
    if user_input == 'B':
        add_course(current_user)
    if user_input == 'C':
        drop_course(current_user)
    if user_input == 'D':
        show_courses(current_user)
    if user_input == 'E':
        save_student_data()
        save_courses_data()
        global LOOP
        LOOP = False

"Find current user we have logged into and assign the appropriate student object"
def user_object():
    for student in STUDENTS:
        if student.getUser() == CURRENT_STUDENT:
            current_user = student
    return current_user

def courses_data():
    "Create course objects"
    courses = ['CS131','CS132','EE210','EE310','Math320','Math220']
    for subject in courses:
        course = Course(subject)
        COURSES.append(course)
    
    "Save CI.txt data into course objects"
    with open("CI.txt", 'r') as opened_file:
        file = opened_file.read().splitlines()
        for line in file:
            if line[0:17] == "COURSES,STUDENTS":
                continue
            courses_students = line.split(',')
            for course in COURSES:
                if course.getcourseName() == courses_students[0]:
                    try:
                        for student in courses_students[1:]:
                            course.addStudent(student)
                    except:
                        continue

def student_data():
    "Create list containing student objects"
    for username in USERNAME_LIST:
        student = Student(username)
        STUDENTS.append(student)
    
    "Save SI.txt data into student objects"
    with open("SI.txt", 'r') as opened_file:
        file = opened_file.read().splitlines()
        for line in file:
            if line[0:17] == "USERNAME,COURSES":
                continue
            username_courses = line.split(',')
            for student in STUDENTS:
                if student.getUser() == username_courses[0]:
                    try:
                        for course in username_courses[1:]:
                            student.addCourse(course)
                    except:
                        continue

"1. Write the userid, and password into the file"
def update_account_file(userid, password):
    with open('UD.txt','a') as file:
        file.write("\n")
        file.write(userid)
        file.write(",")
        file.write(password)

"""1. Create userid with the first char of first name, first two char of last name, and
first three digits of id
2. Have user input password, and then reenter"""
def create_account():
    account_information = (str(input("Please enter your first name, last name, and student ID, separated by a space”.\n")))
    account_data = account_information.split(" ")
    if len(account_data) != 3:
        print("Wrong input format")
        create_account()
    
    first, last, id = account_data[0][0:1], account_data[1][0:2], account_data[2][0:3]
    userid = first.lower() + last.lower() + id.lower()   
    while True:
        password = (str(input("Please enter password.\n")))
        reenter_password = (str(input("Please reenter password: ")))
    
        if password == reenter_password:
            print("User created")
            update_account_file(userid, password)
            USERNAME_LIST.append(userid)
            PASSWORD_LIST.append(password)
            return
        else:
            print("Passwords did not match")

"""1. Have user input their username
2. Run a for loop inside of username_list to make sure username is valid
3. If valid, have user input their password"""
def login():
    index = 0
    username = (str(input("Please enter your user name and hit enter.\n")))   
    for user_checker in USERNAME_LIST:
        if username == user_checker:
            password = (str(input("Enter password.\n")))
            if password == PASSWORD_LIST[index]:
                print("You are logged in")
                global CURRENT_STUDENT, LOOP
                CURRENT_STUDENT = username
                LOOP = False
            else:
                print("Wrong Password")
            return
        index = index + 1 
    
    print("User not found")

"""1. Ask user if they want to login or create a new user
2. Based on their answer, call the login or create account functions"""
def user_begin():
    user_choice = (str(input("Login or create a new user? Select L to login, select C to create new user.\n"))) 
    if user_choice == "L":
        login()
    elif user_choice == "C":
        create_account()

"""1. Open file, collect and store login information
2. Run login/create account function until user has successfully logged in
3. Create student/course objects and store saved data into them
4. Run user schedule manager function"""
def main():
    global LOOP
    with open("UD.txt", 'r') as opened_file:
        file = opened_file.read().splitlines()
    for line in file:
        if line[0:18] == "USERNAME,PASSWORD":
            continue
        username_password = line.split(',')
        USERNAME_LIST.append(username_password[0])
        PASSWORD_LIST.append(username_password[1])  
    while LOOP:
        user_begin()

    student_data()
    courses_data()
    current_user = user_object()
    LOOP = True
    while LOOP:
        manage_schedule(current_user)
    
main()