def main():
    score = validate_score()
    menu()
    choice = input(">>> ").lower()

    while choice != "q":

        if choice == "g":
            score = validate_score()
        elif choice == "p":
            score_state = determine_score(score)
            print(score_state)
        elif choice == "s":
            display_stars(score)
        else:
            print("Choice is not valid.")

        menu()
        choice = input(">>> ").lower()

    print("Have a nice day.")


def menu():
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def display_stars(score):
    score_in_stars = "*" * score
    print(score_in_stars)  # function for displaying stars


def determine_score(score):  # function for determining a grade based on a score
    if score < 50:
        score_result = "Bad"
    elif score < 90:
        score_result = "Passable"
    else:
        score_result = "Excellent"
    return score_result


def validate_score():  # function for validating an inputted score
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Score is not valid. Please try again.")
        print()
        score = int(input("Score: "))
    print("Score is valid.")
    print()
    return score


main()
