# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


# dictonaries = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(dictonaries)

# brand = word
# ford = meaning

# Keys = values

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict["brand", "model", "year"]) x
# print(thisdict["brand"])
# print(thisdict["model"])
# print(thisdict["year"])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020 #update
# }
# print(len(thisdict))

# Dictionary Items - Data Types: The values in dictionary items can be of any data type:

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# # print(thisdict["electric"])
# # print(thisdict["colors"])

# # x = thisdict.keys()
# x = thisdict.values()
# print(x)

# Keys = values


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print(car)