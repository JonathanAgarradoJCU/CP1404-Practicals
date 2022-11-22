"""
Name: Jonathan Roi Ferrer Agarrado (14275360)
CP1404/CP5632 - Practical 02
"""

import random


def main():
    user_score = get_score()
    print()
    while validate_score(user_score) is False:
        user_score = get_score()
    print(f"Inputted score generated: {user_score:.0f}%")
    print(calculate_result(user_score))


def display_random_score():
    random_score = random.randint(0, 100)
    print(f"Random score generated: {random_score:.0f}%")
    print(calculate_result(random_score))


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
