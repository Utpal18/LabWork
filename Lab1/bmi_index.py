# Calculating BODY MASS INDEX(BMI)
# Formula: BMI=mass(in kg)/height (in m^2)

mass=float(input("Enter your mass in kg: ")) # Inputs weight of a person
height=float(input("Enter your height in meter: ")) # Inputs height of a person
BMI=(mass/(height**2)) # Calculates BMI
print("The Body Mask Index is: ",BMI) # Prints the output