#Largest of three numbers

def largest(n1,n2,n3):
    largest = n1
    if(n2>largest):
        largest=n2
    if(n3>largest):
        largest=n3
    return largest
num1,num2,num3=map(int,input().split(","))
print(largest(num1,num2,num3))