from pathlib import Path

#creating a path
# p = Path("data/file.txt")
# print(p)

# windows
# p2 = Path(r"C:\Users\Amar\doc")
# print(p2)


#mac/linux
# p3 = Path("home/amar/doc")
# print(p3)


#current working directory :Current active directory where your script is running  


# cwd = Path.cwd()
# print(cwd)

#home dir

# home = Path.home()
# print(home)

# joining path: This "/" is NOT division here, it's path joining.


# base = Path("project")
# file_path = base / "data" / "input.txt"

# / → Creates correct path automatically, based on the os you are using

# print(file_path)


p = Path("project/data/input.txt")
# does path exist?

# print(p.exists())

# Is it a file or folder?

# print(p.is_file())
# print(p.is_dir())

# print(p.resolve())
# print(p.absolute())

# Useful parts of a path
# p = Path("project/data/input.txt")

# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.suffixes)
# print(p.parent)
# print(p.parents)

#? Changing file name / extension
# p = Path("data/input.txt")
# new_p = p.with_name("output.txt")
# print(new_p)


# Change suffix (extension)
# new_p = p.with_suffix(".csv")
# print(new_p)

#? Listing files and folders
# List immediate contents

# folder = Path(r"D:\python\Unit14\Code")
# # folder.iterdir()

# for item in folder.iterdir():
#     # print(item)
#     if item.is_file():
#         print(item.name)



#? Pattern searching
# folder = Path(r"D: \python\Unit 14\Code")

# # for item in folder.rglob("*.txt"):
# # print(item)


# for item in folder.rglob("*.txt"):
#     print(item)


#? Renaming & Deleting
p = Path(r"D:\python\Unit14\Code\1.txt")
p.rename("new.txt")

p.unlink(missing_ok=True)

p = Path(r"D:\python\Unit14\Code\1.txt")
p.rmdir()
