"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        parts = process_data(line)
        display_data(parts)
        print("----------")
    input_file.close()


def process_data(line):
    """This function is to process the data"""
    print(line)  # See what a line looks like
    print(repr(line))  # See what a line really looks like
    line = line.strip()  # Remove the \n
    parts = line.split(',')  # Separate the data into its parts
    print(parts)  # See what the parts look like (notice the integer is a string)
    parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
    print(parts)  # See if that worked
    return parts


def display_data(parts):
    print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")


main()
