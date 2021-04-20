" Print sum of 3 numbers.If any of the two numbers are same, sum will be 0"

a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))

if a==b or a==c or b==c:
    print("Sum is 0")
else:
    print(a+b+c)
