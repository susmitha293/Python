# 0!=1 , 1!=1
# 5!=5*4*3*2*1=120

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
num=int(input())
print(factorial(num))