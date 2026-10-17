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

# set1 = {"apple", "banana", "cherry"}

# print("banana" in set1) # True 
# print("banana" not in set1) # False


# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# intersection = {"Apple", "Banna", "Banna", "orange", "mango", "orange"} # display - banna, orange
# print(set())

# Union
# The union() method returns a new set with all items from both sets.

# set1 = {"a", "b", "c",}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2
# print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)

# myset = set2.union(set1, set3, set4)
# print(myset)


# set2 = {1, 2, 3}
# set2.union(set1, set3)

# Update
# The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.update(y)

# print(x)


# Intersection
# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3)

interscSet1 = {1,2,3,4}
interscSet2 = {5,4,7,8}

interscSet3 = interscSet1.intersection(interscSet2)
# print(interscSet3)

# | - set
# # & - intersection

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)


# set1 = {"apple", 1,  "banana", False, "cherry"}
# set2 = {0, "google", True, "apple", 2, True}

# # False = 0
# # True = 1

# set3 = set1.intersection(set2)

# print(set3) # 1, apple

