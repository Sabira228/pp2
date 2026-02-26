import json



# JSON string
x = '{ "name":"John", "age":30, "city":"New York"}'

# Convert JSON string to Python dictionary
y = json.loads(x)
print(y["age"])




p = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
j = json.dumps(p)
print(j)




with open("data.json", "w") as file:
    json.dump(p, file)



with open("data.json", "r") as file:
    data = json.load(file)
    print(data)