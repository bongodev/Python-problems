# read all files in directory
# get a list of rolls who have submitted
# check from input if roll has submitted their work

import os

files = os.listdir("submissions")

submitted_rolls = []

for file in files:
    divs = file.split("_")
    roll = divs[1]
    submitted_rolls.append(roll)


while True:
    roll_to_check = input(
        "Please enter which roll to check. Enter q or CTRL+C to exit! "
    )

    if roll_to_check == "q":
        exit(0)

    if roll_to_check in submitted_rolls:
        print(f"Roll {roll_to_check} has submitted their work!")
    else:
        print("faki dise")

# one - add try catch to handle CTRL+C
# given a filename, find its format/extension
# problem 40
