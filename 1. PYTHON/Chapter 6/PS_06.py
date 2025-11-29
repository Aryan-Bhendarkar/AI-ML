mark = int(input("Enter the Mark :: "))
if(mark >= 90 and mark <= 100):
    grade = 'Ex'

elif(mark >= 80 and mark < 90):
    grade = 'A'

elif(mark >= 70 and mark < 80):
    grade = 'B'

elif(mark >= 60 and mark < 70):
    grade = 'C'

elif(mark >= 50 and mark < 60):
    grade = 'D'

else:
    grade = 'F'

print("Your grades are :: " + grade)