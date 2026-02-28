# An even number leaves remainder 0 when divided by 2.
# An odd number leaves remainder 1 when divided by 2.

def check_even_odd(n):
    if(n%2==0):
        return "Even Number"
    else:
        return "Odd Number"

num = int(input("Enter number : "))
result = check_even_odd(num)
print(result)