# Create a tuple
mytuple = ("apple", "banana", "cherry")

# Get an iterator from the tuple
myit = iter(mytuple)

# next() returns the next item in the iterator
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator using a for loop
for x in mytuple:
    print(x)



# A generator function uses the 'yield' keyword
# It returns values one by one instead of all at once

def my_generator():
    yield 1
    yield 2
    yield 3

# Loop through generator
for value in my_generator():
    print(value)

# Using next() with generator
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))




# Similar to list comprehension but uses parentheses
gen_exp = (x * 2 for x in range(5))

for num in gen_exp:
    print(num)