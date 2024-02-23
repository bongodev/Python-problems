# inheritance - OOP


class Animal:
    def __init__(self):
        self.legs = 4

    def speak(self):
        print("animal dake")


class Cow(Animal):
    # def __init__(self):
    #     self.legs = 4

    def speak(self):
        print("hamba")

    def jabor_kata(self):
        print("eating")


class Goat(Animal):
    def __init__(self):
        self.legs = 3

    def beshi_dake(self):
        print("baa baaa")


goru = Cow()
sagol = Goat()

print(goru.legs)
print(sagol.legs)
goru.speak()
sagol.speak()
