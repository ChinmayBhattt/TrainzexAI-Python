# mylist = ["Apple", "Banana", "Mango"]
           # -3.       -2.       -1

# print(mylist[-2]) #Apply why?
# #forward indexing or revese indexing
# # Reverse Indexing - Start - 
# # Forward Indx - 0

# print(mylist[0]) # -3
# print(mylist[-3]) # 0

#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

#If you add new items to a list, the new items will be placed at the end of the list.



# mylist1 = ["Apple", "Banana", "Mango"] # 3 string , not single string
# mylist2 = "Apple Banana Mango" # single string

# print(len(mylist1)) # 3
# print(len(mylist2)) # 18


str1 = ["apple", "banana", "cherry"] 
num = [1, 5, 7, 9, 3]
bool1 = [True, False, False]

# print(type(str1))
# print(type(num))
# print(type(bool1))

list1 = ["abc", 34, True, 40, "male"]
# print(list1[2:5])

# Using the list() constructor to make a List:

# thislist = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(type(thislist))

# tuple = ()
# set = {}
# list = []


# list = change
# a = ["Physics", "Chemistry", "Math"]
# a.insert(1, "bio")

# # a[1] = "Bio"
# print(a)

# a = ["apple", "banana", "cherry"]

# print("before", a)

# a.append("orange") # add

# print("after", a)

# thislist = ["apple", "banana", "cherry"]

# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)
# print(thislist)


# a = ["apple", "banana", "cherry"]

# a.remove("banana")
# print(a)

# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# thislist.pop(1) #  - delete
# print(thislist)


# print(thislist)

# list1 = ["apple", "banana", "cherry"]
# for x in list1:
#   print(x)

"""Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
 """

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# b k m o p

thislist.sort()
print(thislist)

# a = [5,3,1,6,8] # [1,3,5,6,8]
# print(a)

# a.sort()
# print(a)