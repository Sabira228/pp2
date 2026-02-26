import datetime




# datetime.now() returns current date and time
x = datetime.datetime.now()
print(x)

# Access specific parts
print(x.year)          # current year
print(x.strftime("%A"))  # day of the week



# Create a specific date (year, month, day)
y = datetime.datetime(2020, 5, 17)
print(y)




# strftime() formats date into readable string
print(x.strftime("%B"))  # full month name




d1 = datetime.datetime(2023, 1, 1)
d2 = datetime.datetime(2023, 1, 10)

difference = d2 - d1
print(difference)  # shows timedelta