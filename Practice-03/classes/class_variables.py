# Class Variables Example

class Person:
    # Class variable
    country = "Kazakhstan"

    def __init__(self, name):
        self.name = name  # Instance variable


# Create objects
p1 = Person("Sabira")
p2 = Person("Alex")

print(p1.name)       # Sabira
print(p2.name)       # Alex

# Access class variable
print(p1.country)    # Kazakhstan
print(p2.country)    # Kazakhstan

# Change class variable
Person.country = "USA"

print(p1.country)    # USA
print(p2.country)    # USA
