names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate(): gives index and value
print("enumerate():")
for index, name in enumerate(names, start=1):
    print(index, name)

# zip(): combine two lists
print("\nzip():")
for name, score in zip(names, scores):
    print(name, score)

# More built-in examples
letters = ["a", "b", "c"]
numbers = [1, 2, 3]

paired = list(zip(letters, numbers))
print("\nPaired list:", paired)

# sorted with strings
words = ["banana", "apple", "cherry"]
print("sorted words:", sorted(words))