from pathlib import Path

#creating a path
# p = Path("data/file.txt")
# print(p)

# # windows
# p2 = Path(r"C:\Users\Amar\doc")
# print(p2)


# #mac/linux
# p3 = Path("home/amar/doc")
# print(p3)


#cwd = current working directory :Current active directory where your script is running  

# cwd = Path.cwd() # /Users/chinmaybhatt/Python/check
# # print(cwd) # current directory

# home = Path.home() # /Users/chinmaybhatt
# print(home)# home directory


# joining path: This "/" is NOT division here, it's path joining.

# base = Path("project") # folder or file
# file_path = base / "data" / "input.txt"

# print(file_path)
# /Users/chinmaybhatt
# project/data/input.txt
# folder / folder / file

# project/data - none txt file, .txt
# folder / file

# / → Creates correct path automatically, based on the os you are using : mac , linux, windows

# p = Path("project/data/input.txt")
# does path exist?

# print(p.exists()) # False
# p.exists()

# Is it a file or folder?

# print(p.is_file()) # false
# print(p.is_dir()) # true or false - false

# print(f"Resolve: {p.resolve()}")
# print(f"Absolute: {p.absolute()}")

# Useful parts of a path
# p = Path("project/data/input.txt") # path

# input.txt - file name with extention , stem - file name
# suffix - extension - .txt

# print("Name", p.name) # input.txt
# print("STEM", p.stem) # input
# print("suffix ",p.suffix) # .txt
# print("suffixes",p.suffixes) # # [.txt, .dox, .csv]
# print("parent",p.parent) # project/data
# print("parent", p.parents) # <PosixPath.parents>

# name - single person
# names - a lot

# cow - one animal
# cows - multiple



#? Changing file name / extension
# p = Path("data/input.txt") # .txt
# print("Before", p)

# # new_p = p.with_name("output.txt")
# # print("after", new_p)

# # Change suffix (extension) 
# new_p = p.with_suffix(".csv") # .csv # convert
# print(new_p) # print -> extention - .csv ? : 

# input.txt -> input.csv , with_suffix

# ? Listing files and folders
# List immediate contents

# cwd = Path.cwd()
# print(cwd)

folder = Path("/Users/chinmaybhatt/Python")
# folder.iterdir()

# for item in folder.iterdir():
#     # print(item)
#     if item.is_file(): # is_file -> file exist or not 
#         print(item.name)

#? Pattern searching

# # for item in folder.rglob("*.txt"):
# # print(item)


for item in folder.rglob("*.txt"):
    print(item)


#? Renaming & Deleting
p = Path(r"/Users/chinmaybhatt/Python/check")
# p.rename("new.txt")

p.unlink(missing_ok=True)

# p = Path(r"D:\python\Unit14\Code\1.txt")
# p.rmdir()
