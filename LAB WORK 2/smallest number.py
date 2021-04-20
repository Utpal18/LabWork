num1=2
num2=4
num3=5
if num1<num2 and num1<num3:
    smallest=num1
elif num2<num1 and num2<num3:
    smallest = num2
else:
    smallest = num3
print(f'smallest number is {smallest}')