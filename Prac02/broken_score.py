"""
Name: Jonathan Roi Ferrer Agarrado (14275360)
CP1404/CP5632 - Practical
Broken program to determine score status
"""

#  new

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))

if score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")
