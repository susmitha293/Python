# swap without temp

def swap(a,b):
    a,b=b,a
    return a,b
num1,num2=map(int,input().split(","))
num1,num2=swap(num1,num2)
print("After Swapping :")
print("num1 :",num1)
print("num2 :",num2)