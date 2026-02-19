# Method Overriding Example

class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    # This method overrides the parent method
    def speak(self):
        print("The dog says: Woof!")


# Create objects
animal = Animal()
dog = Dog()

animal.speak()  # Parent method
dog.speak()     # Overridden method
