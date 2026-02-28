def palindrome(n):
    original=n
    rev=0
    n=abs(n)
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    return original==rev
    # if(original==rev):
    #     return True
    # else:
    #     return False
num=int(input())
print(palindrome(num))