def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a = int(input('Enter the first number: '))        
b = int(input('Enter the second number: '))        
c = int(input('Enter the third number: '))

d = greatest(a,b,c)
print(d, " is the greatest")