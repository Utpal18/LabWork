weight=float(input("Enter your weight: "))
SIUnit=input("Is the weight in kg or lbs? ")
if SIUnit=="kg":
    new_weight=weight*2.2
    print(f'Your weight in pound is {new_weight}')
elif SIUnit=="lbs":
    new_weight=weight/2.2
    print(f'Your weight in kilogram is {new_weight}')
else:
    print("No Valid Input")
