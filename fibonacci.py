# In Fibonacci, each number is the sum of the previous two numbers.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
# seconf function returns nth fin number as 7 is 13

def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a, end=" ")
        c=a+b
        a=b
        b=c
num=int(input())
fibonacci(num)

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         c = a + b
#         a = b
#         b = c
#     return a
# num = int(input("Enter n: "))
# print(fibonacci(num))