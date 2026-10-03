# The Ternary Operator: The ternary operator allows you to assign one value if a condition is true, and another if it is false:


# a = 5

# if a :
#     print("val of a")
# else:
#     print("value")

# 1. lots of lines (LOC - Line of code)
# 2. Complex

# if a:
#     pass
# elif b:
#     pass
# elif c:
#     pass
# elif d:
#     pass


# The Ternary Operator: 

# num = 3

# x = "WEEKEND!" if num > 5 else "Workday"

# print(x)



# num = 3

# if num > 5:   # False
#     print("WEEKEND")
# else:
#     print("Workday")

# 1. lots of lines (LOC - Line of code) LOC - 6 Lines
# 2. Complex


num = 3

x = "WEEKEND!" if num > 5 else "Workday" # LOC = 1

print(x)


# "Val2" if num > 5 else "Val2" # False

#  "Val1 " <- if ->  "Val2"
# # True <- display
# # False -> Display

num = 5

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)