"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
"""

set1 = {"Shyam", "Neha", "Muskan", "Rohan"}

# set1[0] = "Kartik"

# for i in set1:
#     print(i)
# change, why?


# 1. Repeat - display
# 2. suffle - random
# 3. set const, cant change 

# list and tuple - change

# set2 = {1,2,3,4,5,6,6,7}
# set1 = {"Shyam", "Neha", "Muskan", "Rohan", "Muskan"}

# print(set1)

set1 = {"apple", "banana", "cherry"}

print("banana" in set1) # True 
print("banana" not in set1) # False