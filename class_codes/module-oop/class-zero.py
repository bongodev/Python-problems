class Cat:
    """A simple attempt to model a cat"""

    def __init__(self, name="janina", age=None):
        self.name = name
        self.age = age

    # # python does not support constructor overloading
    # def __init__(self):
    #     pass

    def sleep(self):
        print(f"{self.name} is now sleeping")

    def eat(self, menu):
        print(f"{self.name} is now eating {menu}")


# classnames always start with a capital letter in python
# init -> initialization -> runs automatically whenever we create a new instance/object of the class
# self -> contains all class variables -> passed to every function call

# let's create an instance of this class
my_cat = Cat("puffy", 6)


print(f"my cat's name is {my_cat.name}.")
print(f"my cat is {my_cat.age} years old.")

# # attributes
# # accessed with dot notation

# print(my_cat.name)
# print(my_cat.daknam)
# my_cat.sleep()
# my_cat.eat("fish")

# Every class and method in python is declared public


# default values for constuctor
anjan_cat = Cat("meow")

print(f"Anjan's cat's name is {anjan_cat.name}.")
print(f"Anjan's cat is {anjan_cat.age} years old.")

rana_cat = Cat()
print(f"Rana's cat's name is {rana_cat.name}.")
print(f"Rana's cat is {rana_cat.age} years old.")

anjan_cat.sleep()


# practice tasks:
# 1:
# Restaurant Class:
# attributes: name, cousine
# methods: describe_restaurant(), status()
# 2:
# make 3 such restaurant instances
# if possible, try to work on default values in __init__
