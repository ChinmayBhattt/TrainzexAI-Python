# import shutil
# import os

# # shutil.copy("main.py", "main2.py")
# # shutil.copy2("main.py", "main2.py")

# # shutil.copytree("Module1", "mytutorial")
# # shutil.move("test/main.py", "main.py")
# os.remove("main2.py")

import shutil

usage = shutil.disk_usage('.')
print(f'Total space: {usage.total // (1024**3)} GB')
print(f'Free space: {usage.free // (1024**3)} GB')

# print(1024**3) #1073741824

# print(5*2)
# print(5**2) # power

# print(2*4) #8
# The exponentiation operator in Python (meaning "raised to the power of").
