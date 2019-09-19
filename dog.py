# page one of the tutorial
class Dog:
    # required properties go inside constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # named functions inside class = methods
    def bark(self):
        print("Woof!")


my_dog = Dog("Tommy", "WatchDog")
my_dog.bark()
