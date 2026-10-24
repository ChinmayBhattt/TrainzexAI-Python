# # Python Debugging Fundamentals
# # Python debugging fundamentals ka matlab hai Python code mein errors ko identify karna, unka reason samajhna, aur unhe fix karna. Ye topic practical exams, viva aur real-world programming ke liye important hai.
# 1. What is Debugging?
# Definition: Debugging is the process of finding, analyzing, and fixing errors (bugs) in a program.

# a = 10
# b = 20
# # print(a + c) # c
# NameError: dosnts exist

# ------------ Types of Errors in Python ------------

# 1. Syntax Error
# if x > 5
#     print(x)

# 2. Runtime Error

# a = 10 / 0 # ZeroDivisionError - infinite
# print(a) # yes or no - yes


# 3. Logical Error

# a = 10
# b = 20
# print(a - b) # yes or no -> no ?: 
# # BODMAS

# 3. Common Debugging Techniques
# A. Print Debugging

# a = 10
# b = 5

# print("a =", a)
# print("b =", b)

# result = a + b
# print("Result =", result)

# B. Reading Error Messages

# age = "20"

# print(age + 5) # int or char
# Error: TypeError

# Reason: String aur integer ko directly add nahi kar sakte.


# C. Using Python Debugger (pdb)


# import pdb

# a = 10
# b = 20

# pdb.set_trace()
# result = a + b

# print(result)


# 4. Debugging Process
# 1. Identify the error

# Error message ya unexpected output dekho.


# 2. Reproduce the problem

# Same inputs se error dobara check karo.


# 3. Find the root cause

# Variables, conditions aur execution flow inspect karo.


# 4. Fix and test

# Code correct karke normal aur edge-case inputs test karo.