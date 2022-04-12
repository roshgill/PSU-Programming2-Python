"Lab 2 Project"

"""1. Take in the userid and password
2. Open the UD.txt file with intention of appending
3. Write the userid, and password into the file"""
def update_account_file(userid, password):
    with open('UD.txt','a') as file:
        file.write("\n")
        file.write(userid)
        file.write(",")
        file.write(password)

"""1. Have user input personal information
2. Use split function to separate the first name, last name, and id into a list
3. Create userid with the first char of first name, first two char of last name, and
first three digits of id
4. Have user input password, and then reenter; if they don't match, run the function again until they do
5. Once done correctly, print user created, update password file with new info, and
send user back to homepage"""
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
            break
        else:
            print("Passwords did not match")
    open_file()

"""1. Have user input their username
2. Run a for loop inside of username_list to make sure username is valid
3. If valid, have user input their password; run loop inside password_list for validity
4. If both are correct, print that they are logged in and exit the program
5. If either are incorrect, print user not found and call the user_start function """
def login(username_list, password_list):
    index = 0
    username = (str(input("Please enter your user name and hit enter.\n")))   
    for user_checker in username_list:
        if username == user_checker:
            password = (str(input("Enter password.\n")))
            if password == password_list[index]:
                print("You are logged in")
            else:
                print("Wrong Password")
            user_start(username_list, password_list)
        index = index + 1
        
    print("User not found")
    user_start(username_list, password_list)

"""1. Ask user if they want to login or create a new user
2. Based on their answer, call the login or create account functions
3. If user's input is incorrect, call user_start function itself"""
def user_start(username_list, password_list):
    user_choice = (str(input("Login or create a new user? Select L to login, select C to create new user.\n")))
    
    if user_choice == "L":
        login(username_list, password_list)
    elif user_choice == "C":
        create_account()
    else:
        user_start(username_list, password_list)

"""1. Open file
2. Use split function to separate the usernames and passwords
3. Append the usernames and passwords into respective lists
4. Send lists into user_display function"""
def open_file():
    with open("UD.txt", 'r') as opened_file:
        file = opened_file.read().splitlines()
    username_list = []
    password_list = []
    
    for line in file:
        if line[0:4] == "USER":
            continue
        username_password = line.split(',')
        username_list.append(username_password[0])
        password_list.append(username_password[1])
    user_start(username_list, password_list)

open_file()