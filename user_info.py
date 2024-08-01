#Creates a user class with validation for username, email, and password? 
#The code should take these inputs from the user, validate them according to specific rules,
#and create a User object with the valid information.
import re

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __str__(self):
        return (f"Username: {self.username}\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}")

def is_valid_username(username):
    pattern = r'^[a-zA-Z0-9._%+-]{1,6}$'
    return re.match(pattern, username) is not None

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_password(password):
    pattern = r'^[a-zA-Z0-9._%+-]{1,6}$'
    return re.match(pattern, password) is not None

def get_user_input():
    while True:
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
       
        if not is_valid_username(username):
            print("Invalid username. Please try again.")
            continue
        elif not is_valid_email(email):
            print("Invalid email address. Please try again.")
            continue

        return User(username, email, password)

print("\nUser Information:")
print(get_user_input())
