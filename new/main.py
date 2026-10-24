# The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the os module.
# import shutil
# import os

# shutil.copy("os.py", "hello.py")
# shutil.copy2("main.py", "main3.py")
# shutil.copytree("Module1", "mytutorial")

# os.remove("os.py")
# # print("Hello world")


import shutil

try:
    shutil.copy("main.py", "main.3py")
    print("File copied successfully")

except FileNotFoundError:
    print("Source file not found")

except PermissionError: # pdf. txt, docx 
    print("Permission denied")

# SBI or HDFC - email - pdf


# # PermissionError
# pdf open - password

# pdf - password manager 
# Information read

# pdf:
# - Bank deatails 
# - Gov document
# - legel papers
# - tax form

# password: 
# email: - password: username@sbi.co.in