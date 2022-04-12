def write_file(username, password):
    with open('UD.txt','a') as file:
        file.write(username)
        file.write(",")
        file.write(password)
        file.write("\n")

def create_user_name(first, last, password):
    username = first[:2].lower() + last[:3].lower()
    print(f'Hi {first}, your user name is {username}')
    write_file(username,password)

def get_password(first, last):
    password = str(input('''Enter password, password should have more than 
8 characters, with at least one digit, 
one symbol, and one uppercase: '''))
    
    if (password != first and len(password) > 8):
        digit_checker = 0
        symbol_checker = 0
        uppercase_checker = 0
        for character in password:
            if ord(character) >= 48 and ord(character) <= 59:
                digit_checker += 1
            if ord(character) >= 32 and ord(character) <= 47:
                symbol_checker += 1
            if ord(character) >= 65 and ord(character) <= 90:
                uppercase_checker += 1
        
        if (digit_checker > 0 and symbol_checker >0 and uppercase_checker > 0):
            password_confirm = (str(input('Please reconfirm password: ')))
            if password == password_confirm:
                create_user_name(first, last, password)
                exit()
        
    print("Did not meet password requirements, re-enter password\n")
    get_password(first, last)
    
def get_user_name():
    first = (str(input('Enter first name: ')))
    last = (str(input('Enter your last name: ')))
    get_password(first, last)

get_user_name()