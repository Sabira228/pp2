# Multiple Inheritance Example

class Father:
    def skills(self):
        print("Gardening, Programming")


class Mother:
    def skills(self):
        print("Cooking, Painting")


class Child(Father, Mother):
    pass


# Create object
child = Child()

# Calls the first parent in the inheritance order
child.skills()
