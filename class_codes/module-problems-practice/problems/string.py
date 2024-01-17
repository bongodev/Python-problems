# Format: name_roll_courseCode_submission.py
word = "hasnine_1200904_cse4201_submission.py"
# find student_name, roll, course

# 1403004
# 1703004
# 133004

# split a string
# print(word.split("_"))  # delimiter

divs = word.split("_")
name = divs[0]
roll = divs[1]
course = divs[2]

print(f"name: {name}, roll: {roll}, course: {course}")

# example = "-------|----|---"
# print(example.split("|"))
