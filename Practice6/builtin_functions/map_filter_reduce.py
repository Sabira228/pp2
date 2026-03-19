from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map(): multiply each element by 2
mapped = list(map(lambda x: x * 2, numbers))
print("map():", mapped)

# filter(): keep even numbers
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("filter():", filtered)

# reduce(): sum all numbers
reduced = reduce(lambda x, y: x + y, numbers)
print("reduce():", reduced)

# Built-in functions
print("len():", len(numbers))
print("sum():", sum(numbers))
print("min():", min(numbers))
print("max():", max(numbers))
print("sorted() descending:", sorted(numbers, reverse=True))

# Type conversions
num_str = "123"
print("int conversion:", int(num_str))

float_str = "3.14"
print("float conversion:", float(float_str))

bool_value = 1
print("bool conversion:", bool(bool_value))

print("type checking:", type(numbers), type(num_str))