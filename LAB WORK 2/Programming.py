list=[]

for i in range(3):

    name=input("Enter your name: ")
    ID_number=input("Enter your ID: ")
    Address=input("Enter your address: ")
    list.append(ID_number)
    list.append(name)
    list.append(Address)

for j in list:
    print(j)
