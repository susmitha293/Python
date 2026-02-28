# swap temp

def temp_swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
a,b=map(int,input("BEFORE SWAPPING : ").split(","))
a,b=temp_swap(a,b)
print("After Swapping : ")
print("a =",a)
print("b =",b)