# Python Functions
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.



# Sister - Function() -> Work - Chai Bana na - Chai Maker
# Daily - ignore - sister - bhul gayi

# sister - function() - Chai

# Called - bolna padhega

# - How to make Chai

# 1. Pani
# 2. Milk
# 3. Chai Patti
# 4. Sugar
# 5. adiotional - astulsi, pudhina  person dont use 

# Function() - Chai
# tum - called function()


# Sister - Chai - called 


a = 5
b = 10
c = a + b

# print(c)

d = 5
e = 6
f = d + e

# print(f)

# 10 Times
# 100 posible - time consuming
# 100000 x 5 LOC()


# def my_function():
#   print("Hello from a function")


# print(my_function())

# # def add():
# #   a = 5
# #   b = 10
# #   return a + b

# # print(add())

# function - values - return 
  


# def sum(a, b):
#     return a + b


def avg(a, b):
    return a + b / 2

# print(avg(5,6))
# print(avg(2,3))


# def good_morning():
#     print("Good morning")

# print(good_morning())

# def good_morning():
#     pass

# print(good_morning())

# def my_function():
#   print("Hello from a function")

# my_function()

# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9


# val = int(input("enter value: "))
# print(fahrenheit_to_celsius(val))

# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# def greet(fname):
#     print(fname + " Sharma")

# greet(" Rohan")
# greet(" Muskan")
# greet(" Yash")

def add(a=5, b=6):
    return a + b

# print(add())

# local Variable
# global valiable a = 5


# def sum():
#    a = 5
#    return a

# a = 10
# print(a)
# print(sum())

# def my_function(name = "friend"):
#   print("Hello", name)

# my_function("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")

# x = 300 #global

# def myfunc():
#   x = 200 # local
#   print(x) # 

# myfunc() # 

# print(x) # 


# Python Decorators
# Decorators let you add extra behavior to a function, without changing the function's code.

# A decorator is a function that takes another function as input and returns a new function.

# Basic Decorator
# Define the decorator first, then apply it with @decorator_name above the function.

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase #decorator
# def myfunction():
#   return "Hello Sally"

# print(myfunction())


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner # ---- Upper

# def addgreeting(func):
#   def myinner():
#     return "Hello " + func() + " Have a good day!"
#   return myinner

# @changecase
# @addgreeting
# def myfunction():
#   return "Tobias"

# print(myfunction())

# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)

