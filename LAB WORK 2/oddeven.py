'''to check if the input number s oddor even'''

num=int(input('enter number'))
even=False
if num%2==0:
    even=True
else:
    even=False

if even:
    print('number is even')
else:
    print('number is odd')