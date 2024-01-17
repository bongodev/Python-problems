def greet_user():
    name = input("What is your name")
    print(f"hello {name}")


def check_age():
    age = int(input("Enter your age: "))
    if age < 12:
        print("Not Allowed!")
    else:
        print("Welcome!")
