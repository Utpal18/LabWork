'''def sub():
    print("Inside Function")
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    if b>a:
        c=b-a
    else:
        c=a-b
    print("Difference: ",c)
    print(f'The difference is: {c}')

print("Calling Function")
sub()
print("Outside Function")'''



'''def sub(a,b):
    if b > a:
        c = b - a
    else:
        c = a - b
        # print("Difference: ", c)
    return c


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
sub(a, b)
# print(sub(a,b))
d = sub(a, b)
print("The difference is: ", d)
'''

def sum():
    a=int(input("a:"))
    b=int(input("b:"))
    c=a+b
    return c
print(sum())
