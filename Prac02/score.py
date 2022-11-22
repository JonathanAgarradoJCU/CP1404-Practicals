import random


def main():
    user_score = get_score()  # get user's input as score
    print()
    while validate_score(user_score) is False:  # validate user's score
        user_score = get_score()
    print(f"Inputted score generated: {user_score:.0f}%")  # display user's score
    print(calculate_result(user_score))  # display user's result


def display_random_score():
    random_score = random.randint(0, 100)  # get random score
    print(f"Random score generated: {random_score:.0f}%")  # display random score
    print(calculate_result(random_score))  # display random score result


def get_score():
    user_score = float(input("Input score: "))
    return user_score


def validate_score(score):
    if score < 0 or score > 100:
        print("Invalid score.")
        return False


def calculate_result(score):
    if score < 50:
        return "Bad"
    elif score < 75:
        return "Passable"
    elif score < 85:
        return "Decent"
    elif score < 100:
        return "Excellent"
    else:
        return "Perfect"


main()
print()
display_random_score()
