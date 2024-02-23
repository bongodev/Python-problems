class User:
    """a basic program user"""

    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.angry = False

    def describe_user(self):
        name = self.first_name + self.last_name
        print(f"Fullname is {name}")

        if self.age is not None:
            print(f"Age is {self.age}")

    def greet_user(self):
        print(f"hello {self.first_name}")

    def mood_kemon(self):
        if self.angry == True:
            print("valo na!")
        else:
            print("valo")

    def make_angry(self):
        self.angry = True

    def make_nice(self):
        self.angry = False


# bongodev = User("bongo", "dev")
# bongodev.describe_user()

# print()

kafka = User("kafka", "tamura", 99)
# kafka.describe_user()

print("shurute")
kafka.mood_kemon()

# directly updating an attribute
# kafka.angry = True
# print("after maramari")
# kafka.mood_kemon()

# update through a function
kafka.make_angry()
print("after ragano")
kafka.mood_kemon()

kafka.make_nice()
print("calmed down!")
kafka.mood_kemon()
