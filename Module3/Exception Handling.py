# Python Exception Handling
# Exception Handling allows a program to handle unexpected errors during execution in a controlled way, instead of crashing abruptly. It enables programs to detect errors, manage them properly and continue execution wherever possible.

# Handles runtime errors such as invalid input, file not found, division by zero and type mismatches that occur during program execution.
# Helps improve program reliability by ensuring the application does not terminate unexpectedly when an error occurs.

# n = 10
# res = n / 0
# print(res)

# n = 10

# try:
#     res = n / 0
# except ZeroDivisionError:
#     print("Can't be divided by zero!")


# try:
#     n = 0
#     res = 100 / n
    
# except ZeroDivisionError:
#     print("You can't divide by zero!")
    
# except ValueError:
#     print("Enter a valid number!")
    
# else:
#     print("Result is", res)
    
# finally:
#     print("Execution complete.")

# try:
#     # This will cause ValueError
#     x = int("str")  # wrong Value 
#     inv = 1 / x   # Inverse calculation
    
# except ValueError:
#     print("Not Valid!")
    
# except ZeroDivisionError:
#     print("Zero has no inverse!")


# 2. Multiple Exceptions

# We can catch multiple exceptions in a single block if we need to handle them in the same way or we can separate them if different types of exceptions require different handling.

# Example: This code attempts to convert list elements and handles ValueError, TypeError and IndexError.


# a = ["10", "twenty", 30] # str, str, int
# try:
#     # 'twenty' cannot be converted to int
#     total = int(a[0]) + int(a[1])   # a[0] = "10", a[1] = "twenty" = a[0] + a[1] = 
    
# except (ValueError, TypeError) as e:
#     print("Error", e)
    
# except IndexError:
#     print("Index out of range.")


# try:
#     # Risky operation: dividing string by number
#     res = "100" / 20 
    
# except ArithmeticError:
#     print("Arithmetic problem.")
    
# except:
#     print("Something went wrong!")



# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# Raise 
# Raise an error and stop the program if x is lower than 0:


# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")