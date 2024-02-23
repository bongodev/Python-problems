# abstraction
class Car:
    def __init__(self):
        pass

    def start(self):
        self.check_engine()

    def check_engine(self):
        # complex code happening here
        print("engine is good")


# Polymorphism
class Bird:
    def speak(self):
        print("Tweet")


class Dog:
    def speak(self):
        print("bark")


bird_obj = Bird()
dog_obj = Dog()

animals = [bird_obj, dog_obj]

for animal in animals:
    animal.speak()
