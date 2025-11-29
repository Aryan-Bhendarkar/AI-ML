a = int(input("Enter the User's age :: "))

if(a>18):
    print("You are eligible 🥳")

elif(a == 0):
    print("You entered Zero, please retry...")

elif(a<0):
    print("Please enter valid age !")
else:
    print("You are not eligible")