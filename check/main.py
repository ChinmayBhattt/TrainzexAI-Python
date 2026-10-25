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

cwd = Path.cwd() # /Users/chinmaybhatt/Python/check
# print(cwd) # current directory

home = Path.home() # /Users/chinmaybhatt
print(home)# home directory


# joining path: This "/" is NOT division here, it's path joining.

base = Path("project") # folder or file
file_path = base / "data" / "input.txt"

print(file_path)
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
p = Path("project/data/input.txt") # path

# input.txt - file name with extention , stem - file name
# suffix - extension - .txt

print("Name", p.name) # input.txt
print("STEM", p.stem) # input
print("suffix ",p.suffix) # .txt
print("suffixes",p.suffixes) # # [.txt, .dox, .csv]
print("parent",p.parent) # project/data
print("parent", p.parents) # <PosixPath.parents>

# name - single person
# names - a lot

# cow - one animal
# cows - multiple