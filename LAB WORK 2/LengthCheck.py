'''
If name is less than 3 characters,name must be at least 3 characters
otherwise if its more than 50 characters,name must be 50 characters max.
otherwise, name looks good
'''

name=input("Enter your name: ")
if len(name)<3:
    print("Your name should be at least  3 characters long")
elif len(name)>50:
    print("Your name should be 50 characters maximum")
else:
    print("Your name looks good")
