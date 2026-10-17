# File handling is an important part of any web application.

# Python has several functions for creating, reading, updating, and deleting files.

# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# f = open('myfile.txt', 'r') # read
# print(f)
# data = f.read()

# print(data)

# f.close()

# f = open('myfile.txt', 'w') # write
# f.write("Hello what are you doing")
# f.close()

# with open('myfile.txt', 'r') as f:
#     data = f.read()
#     print(data)
#     f.close() 

# with open('myfile.txt', 'w') as f:
#     f.write("Hey I am python developer")

# f = open('myfile.txt', 'x') # append
# f.write("Hey I am python developer \n")


# "x" - Create - Creates the specified file, returns an error if the file exists

# with open("demo.txt", 'x') as f:
#     print("File Created!")

# with open("demo.txt", 'w') as f:
#     f.write("Hello world")

# The readline() method in Python reads a single line from a file and returns it as a string. It reads up until it hits a newline character (\n) and includes that newline character at the end of the returned string

# f = open("myfile.txt", "rt")
# data = f.read()

# print(data)
# print(f)

# f = open("myfile.txt", "rb")
# data = f.read()

# print(data)
# # print(f)


# f = open("myfile.txt", 'r')

# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = line.split(",")[3]
#     print(f"marks of students {i} is {m1*4}")
#     print(f"marks of students {i} is {m2 * 5}")
#     print(f"marks of students {i} is {m3}")

# print(type(m1))
# print(type(m2))
# print(type(m3))