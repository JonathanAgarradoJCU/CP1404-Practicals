PASSWORD_LENGTH = 8  # minimum length of typical password


def main():
    password = get_password()  # asks user for input
    while validate_password(password) is False:  # validates input
        password = get_password()
    display_stars(password)  # converts input into stars


def get_password():
    password = input("Input password: ")
    return password


def validate_password(password):
    if len(password) < PASSWORD_LENGTH:
        print(f"Minimum password length is 8 characters! You only typed in {len(password)} character(s).")
        return False


def display_stars(password):
    for i in range(1, len(password) + 1, 1):
        print("*", end='')


main()
