# getting imports and setup
import string
import random
print(" Welcome to the password generator! ")
# Setting up variables
password_length = 12
upcase = string.ascii_uppercase
lowcase = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

# function creation


def pass_create():
    all_characters = upcase + lowcase + digits + special_characters
    password = random.sample(all_characters, password_length)
    password = "".join(password)
    return password


# basic while loop as used in the to do tasks!
while True:
    print("\n Options:")
    print(" [1] - Generate a Password!")
    print("[2] - Quit the password generator")

    choice = input("Enter your choice [1/2]: ")
    if choice == "1":
        print("\n HERE IS YOUR PASSWORD: ")
        password = pass_create()
        print(password)
    elif choice == "2":
        break
    else:
        print("That was not an option, Please try again!")
