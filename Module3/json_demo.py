
# 2\. JSON (JavaScript Object Notation): JSON is a lightweight data-interchange format used to store and exchange structured data using key-value pairs and arrays. In Python, the built-in `json` module is used to read, write, and process JSON data.


# ____________________ JSON processing ____________________


# import json

# student = {
#     "id": 1,
#     "name": "Chinmay",
#     "marks": 85,
#     "passed": True
# }

# with open("myjson.json", "w") as file:
#     json.dump(student, file, indent=4)


# with open("student.json", "r") as file:
#     student = json.load(file)

# print(student)
# print(student["name"])
# print(student["marks"])
# print(student["passed"])


# student = {
#     "name": "Chinmay",
#     "college": {
#         "name": "Arya College",
#         "city": "Jaipur"
#     },
#     "skills": ["Python", "AI", "Web"]
# }

# print(type(student))


# for i in student:
#     print(student[i])


# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# # dump - format condtion {}

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True)) # formate -  no / yes 