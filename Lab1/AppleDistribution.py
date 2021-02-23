'''3. N students take K apple and distribut them among each other evenly.
The remaining undivisible part remains in basket.How many apples do each individual get?How many apples remain in the
basket?'''
number=int(input("Enter number of apples: "))
student=int(input("Enter number of students: "))
if student>number:
    apple=number//student
    remaining_apple=number-(apple*student)
    print("Total apple per student: ",apple)
    print("Apples remaining in basket: ",remaining_apple)






