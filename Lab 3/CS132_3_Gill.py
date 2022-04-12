"User class stores all user information"
class Users:
    def __init__(self, first, last, user, password):
        self.first = first
        self.last = last
        self.user = user
        self.password = password

"Written this way, OBJECTS_LIST is made into a global variable than can be accessed anywhere in our file"
OBJECTS_LIST = []

"1. Have user input information, append it into UD.txt, and store information into Class and append into USERLIST"
def add_user():
    user_input = str(input("Enter user info in the following format: First name,last name,username,password: "))
    with open("UD.txt", 'a') as opened_file:
        opened_file.write("\n")
        opened_file.write(user_input)
    
    user_info = user_input.split(',')
    OBJECTS_LIST.append(Users(user_info[0],user_info[1],user_info[2],user_info[3]))

"1. Based on user input, run specified if-statement"
"2. Save data (as lowercase) into a list and sort it alphabetically"
"""3. We turn them into lowercase because uppercase characters have lower ascii 
numbers than lowercase characters and the result will result in incorrect alphabetic order"""
"4. Compare list and object data and print when both are similar, finish when all data in alphabetic list is sifted through"
def output(user_input):
    if user_input == "D":
        first_names = []
        for users in OBJECTS_LIST:
            first_names.append(users.first.lower())
        first_names = sorted(first_names)
        
        for name in first_names:
            for user in OBJECTS_LIST:
                if name == user.first.lower():
                    print(f"{user.first},{user.last},{user.user},{user.password}")
    
    if user_input == "E":
        last_names = []
        for users in OBJECTS_LIST:
            last_names.append(users.last.lower())
        last_names = sorted(last_names)
 
        for lastname in last_names:
            for user in OBJECTS_LIST:
                if lastname == user.last.lower():
                    print(f"{user.first},{user.last},{user.user},{user.password}")

"1. Based on user input, run specified if-statement"
"2. Have user input specified data and compare with data saved in all objects"
"3. If the object data equals user input, print the current object's information"
def search_function(user_input):
    if user_input == "A":
        last_name = str(input("Enter user’s last name: "))
        for user in OBJECTS_LIST:
            if last_name == user.last:
                print(f"{user.first},{user.last},{user.user},{user.password}")
                return
    elif user_input == "B":
        first_name = str(input("Enter user’s first name: "))
        for user in OBJECTS_LIST:
            if first_name == user.first:
                print(f"{user.first},{user.last},{user.user},{user.password}")
                return  
    elif user_input == "C":
        user_name = str(input("Enter user’s username: "))
        for user in OBJECTS_LIST:
            if user_name == user.user:
                print(f"{user.first},{user.last},{user.user},{user.password}")
                return
    print("Not found")

"1. Present user with command options and execute function based on input given"               
def user_start():
    user_input = str(input("""A: Search by last name\nB: Search by first name\nC: Search by username\nD: Display all users alphabetically by First name\nE. Display all users alphabetically by Last name\nF: Insert a user\n:"""))
    if user_input == "A" or user_input == "B" or user_input == "C":
        search_function(user_input)
    if user_input == "D" or user_input == "E":
        output(user_input)
    if user_input == "F":
        add_user()

"1. Open textfile, split the lines, then split the first,last,username,password for each line into a list"
"2. Store information into user objects, and store objects into a list"
"3. Once all information is secured and stored, run program"
def main():
    with open("UD.txt", 'r') as opened_file:
        new_file = opened_file.read().splitlines()
        for line in new_file:
            if line[0:38] == "FIRST NAME,LAST NAME,USERNAME,PASSWORD":
                continue
            user_info = line.split(',')
            OBJECTS_LIST.append(Users(user_info[0],user_info[1],user_info[2],user_info[3]))

    while True:
        user_start()

main()