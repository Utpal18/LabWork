'''
1.Check whether 5 is in the list of first five natural numbers or not.(Hint list=(1,2,3,4,5)
'''
list=[1,2,3,4,5]
a=5
for i in list:
    if i == a:
        c=1
if c==1:
    print(f'{a} is in the list')
else:
    print(f'{a} is not in the list')

