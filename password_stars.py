"""
On paper, write a program that asks the user for a password, with error-checking
to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.
"""

PASSWORD_LENGTH = 8  # minimum length of typical password


def main():
    password = get_password()  # ask user for input
    while validate_password(password):  # validate input
        password = get_password()
    display_stars(password)  # convert input into stars


def get_password():
    password = input("Input password: ")
    return password


def validate_password(password):
    if len(password) < PASSWORD_LENGTH:
        print(f"Minimum password length is 8 characters! You only typed in {len(password)} character(s).")
        return True


def display_stars(password):
    for i in range(1, len(password) + 1, 1):
        print("*", end='')


main()
