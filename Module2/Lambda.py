# Lambda Functions
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression


# def add(a):
#     return a + 10

# print(add(5))


# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))


# avg = lambda a, b : (a + b) / 2 # lambda = function

# print(avg(8,4)) # 8 + 4 = 12 / 2 = 6

# print("before", type(avg))
# print(int(avg(8,4))) 
# print("after", type(avg))


# sum = lambda


# num = [1,2,3,4,5]

# sqaure = lambda x: x * 2

# for n in num:
#     print(sqaure(n))
 


is_even = lambda x: x % 2 == 0

for i in range(1, 11):
    if is_even(i):
        print(f"Is even?: {i}")