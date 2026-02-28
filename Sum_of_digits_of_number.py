# Sum of digits of number

def sum_digits_number(n):
    n=abs(n)
    total=0
    while(n>0):
        digit=n%10
        total+=digit
        n=n//10   #gives divisor
    return total
num=int(input())
print(sum_digits_number(num))