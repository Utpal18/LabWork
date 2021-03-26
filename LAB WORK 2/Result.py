'''
2.WAP which accepts marks of 4 subjects and display total marks, percentage and grade
'''
a=int(input("Enter marks for 1st subject: "))
b=int(input("Enter marks for 2nd subject: "))
c=int(input("Enter marks for 3rd subject: "))
d=int(input("Enter marks for 4th subject: "))
MarksObtained=a+b+c+d
total=400
percentage=(MarksObtained/total)*100
if percentage<=100 and percentage>=90:
    print("Your grade is A+")
elif percentage>=80 and percentage<90:
    print("Your grade is A")
elif percentage >= 70 and percentage < 80:
    print("Your grade is B")
elif percentage >=60 and percentage < 70:
    print("Your grade is C")
elif percentage >= 50 and percentage <60:
    print("Your grade is D")
elif percentage >=40 and percentage <= 50:
    print("Your grade is E")
else:
    print("You've failed")










