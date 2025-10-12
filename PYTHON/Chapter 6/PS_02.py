Mark1 = int(input("Enter marks for subject 1 :: "))
Mark2 = int(input("Enter marks for subject 2 :: "))
Mark3 = int(input("Enter marks for subject 3 :: "))

total = (Mark1 + Mark2 + Mark3)/3

if(total >= 40 and Mark1 >= 33 and Mark2 >= 33 and Mark3 >= 33):
    print("Student has Passed in Exam 🥳🥳" + total)

else:
    print("Student Failed in the Exam 😔😔" + total)