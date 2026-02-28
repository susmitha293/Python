# A number is prime if:
# It has exactly 2 factors only → 1 and itself.

def prime_num(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
num=int(input())
print(prime_num(num))