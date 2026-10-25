# class person:
#     name = "chinmay"
#     occupation = "software developer"
#     networth = 10

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a = person()
# b = person()
# b.name = "nikita"

# # a.name = "shyam"
# # a.occupation = "accounted"
# # print(a.name, a.occupation)

# a.info()
# b.info()


class person:

    def __init__(self, n ,o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("chinmay", "HR")

a.info()