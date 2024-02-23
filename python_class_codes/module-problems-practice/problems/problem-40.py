# 40. **Password Validator**: Write a program that validates a password based on specific criteria.


# criteria here: one small letter, one capital, one digit, length 8-20
# our task is to check if a string has one small letter, one capital, one digit and length is between 8-20


password = "admin1dmiN"


def checkPassword(password):
    if len(password) < 8 or len(password) > 20:
        return False

    chotoLetterAse = 0
    boroLetterAse = 0
    digitAse = 0

    for letter in password:
        if letter.islower():
            chotoLetterAse = 1
        if letter.isupper():
            boroLetterAse = 1
        if letter.isdigit():
            digitAse = 1

    if chotoLetterAse == 0 or boroLetterAse == 0 or digitAse == 0:
        return False

    return True


if checkPassword(password):
    print("Good password")
else:
    print("Bad password")


# try to use a loop to take user input and close on ctrl c
