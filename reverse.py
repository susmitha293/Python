# def reverse_num(n):
#     rev=0
#     while(n>0):
#         d=n%10
#         rev=rev*10+d
#         n=n//10
#     return rev
# num=int(input())
# print(reverse_num(num))


def reverse_num(n):
    if(n<0):
        sign=-1
    else:
        sign=1
    n = abs(n) 
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev*sign
num=int(input())
print(reverse_num(num))