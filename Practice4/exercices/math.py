import math
import random



print(min(5, 10, 25))   # smallest value
print(max(5, 10, 25))   # largest value
print(abs(-7.25))       # absolute value
print(round(3.6))       # round number
print(pow(4, 3))        # 4 to the power of 3




print(math.sqrt(64))     # square root
print(math.ceil(1.4))    # round up
print(math.floor(1.4))   # round down
print(math.pi)           # value of pi
print(math.e)            # Euler's number



print(random.random())      # random number between 0 and 1
print(random.randint(1, 10))  # random integer

numbers = [1, 2, 3, 4]
random.shuffle(numbers)      # shuffle list
print(numbers)