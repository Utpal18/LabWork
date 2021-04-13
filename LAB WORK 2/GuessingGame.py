number=10
trial=1
while trial<=3:
    trial = trial + 1
    print("You have to guess the number")
    num=int(input("Enter the number between 1-20: "))
    if num==number:
        print("You have guessed the correct number")
    elif trial==4:
        print("You failed")
    else:
         print("Try Again")




