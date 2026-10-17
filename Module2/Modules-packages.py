# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# import mymodule as mx

# mx.greeting("Jonathan")

# import platform

# x = platform.system()
# print(x)

# Using the dir() Function :There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# import mymodule

# x = dir(mymodule)
# print(x)

from mymodule import person1
print (person1["age"])
