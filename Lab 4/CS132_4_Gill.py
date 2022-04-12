"User class stores all user information"
class Userdata:
    def __init__(self):
        self.__first = ''
        self.__last = ''
        self.__user = ''
        self.__password = ''
    
    def set_firstname(self, first):
        self.__first = first
    def get_firstname(self):
        first = self.__first
        return (first)
    
    def set_lastname(self, last):
        self.__last = last
    def get_lastname(self):
        last = self.__last
        return (last)
    
    def set_username(self, user):
        self.__user = user
    def get_username(self):
        user = self.__user
        return (user)
    
    def set_password(self, password):
        self.__password = password
    def get_password(self):
        password = self.__password
        return (password)
    
    def display_all_users(self):
        print(self.__first + " " + self.__last + " " + self.__user + " " + self.__password)

"Written this way, OBJECTS_LIST is made into a global variable than can be accessed anywhere in our file"
OBJECTS_LIST = []         

def create_object(user_info):
    user = Userdata()
    user.set_firstname(user_info[0])
    user.set_lastname(user_info[1])
    user.set_username(user_info[2])
    user.set_password(user_info[3])
    OBJECTS_LIST.append(user)

"1. Have user input information, append it into UD.txt, and store information into Class and append into USERLIST"
def add_user():
    user_input = str(input("Enter user info in the following format: First name,last name,username,password: "))
    with open("UD.txt", 'a') as opened_file:
        opened_file.write("\n")
        opened_file.write(user_input)
    
    user_info = user_input.split(',')
    create_object(user_info)

# "1. Based on user input, run specified if-statement"
# "2. Have user input specified data and compare with data saved in all objects"
# "3. If the object data equals user input, print the current object's information"
def search_function(user_input):
    if user_input == "A":
        last_name = str(input("Enter user’s name in the form: Lastname: "))
        for user in OBJECTS_LIST:
            if last_name == user.get_lastname():
                print(f"Password is {user.get_password()}")
                return
    elif user_input == "B":
        user_name = str(input("Enter user’s username: "))
        for user in OBJECTS_LIST:
            if user_name == user.get_username():
                print(f"Password is {user.get_password()}")
                return
    print("Not found")

"1. Present user with command options and execute function based on input given"               
def user_start():
    user_input = str(input("""A: Search by last name\nB: Search by username\nC: Insert a user\nD: Display all users\n:"""))
    if user_input == "A" or user_input == "B":
        search_function(user_input)
    if user_input == "C":
        add_user()
    if user_input == "D":
        print("FIRST,LAST,USERNAME,PASSWORD")
        for user in OBJECTS_LIST:
            user.display_all_users()
    if user_input != 'A' and user_input != 'B' and user_input != 'C' and user_input != 'D':
        print("Enter a valid option")
    
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
            create_object(user_info)

    while True:
        user_start()

main()