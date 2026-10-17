# ____________________ files handling ____________________

# # f = open('myfile.txt', 'r') 
# f = open('myfile.txt') # r is default
# # f = open('myfile.txt', 'rt') # as a text file open
# f = open('myfile.txt', 'rb') # as a binary

# txt = f.read()
# print(txt)
# f.close()

# -----

# f = open('myfile.txt', 'a')
# f = open('myfile.txt', 'w')
# f.write("Hello world")
# f.close()

# -----

# with open('myfile.txt', 'a') as f:
#     f.write('Hey i am new ')

# -----# -----# -----# -----# -----# -----# -----

# f = open("myfile.txt", 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[0]
#     print(f"marks of students {i} is {m1*4}")
#     print(f"marks of students {i} is {m2}")
#     print(f"marks of students {i} is {m3}")

# print(type(m1))
# print(type(m2))

# -----# -----# -----# -----# -----# -----# -----


f = open("myfile2.txt", 'w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()
# ____________________ os ____________________


#os

# import os 
# # os.mkdir("data")

# if(not os.path.exists()):
#     os.mkdir("data")

# for i in range(1,10):
#     os.mkdir(f"Data/Day {i+1}")




# import os
# # os.mkdir("Data")

# for i in range(1,10):
#     os.mkdir(f"Data/Day {i+1}")


# import os
# # os.mkdir("Data")
# # if(not os.path.exists()):
# #     os.mkdir("Data")

# for i in range(0,10):
#     os.rename(f"Data/New {i+1}", f"Data/Create {i+1}")


# import os
# folders = os.listdir("Data")

# # print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Data/{folder}"))



# ____________________ Pathlib ____________________
# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())


# from pathlib import Path
# # Creating
# p1 = Path("data/file.txt")
# # print (p1)
# # Windows-style absolute path (raw string)
# p2 = Path(r"C:\Users\Amar\doc")
# print (p2)
# # Linux/mac absolute path
# p3 = Path("/home/amar/doc")
# print (p3)