"""

On paper, write a program that asks the user for a password, with error-checking
to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.

"""

PASSWORD_LENGTH = 8  # minimum length of typical password

user_password = input("Input password: ")
while len(user_password) < PASSWORD_LENGTH:
    print("Minimum password length is 8 characters!")
    user_password = input("Input password: ")

for i in range(1, len(user_password) + 1, 1):
    print("*", end='')
