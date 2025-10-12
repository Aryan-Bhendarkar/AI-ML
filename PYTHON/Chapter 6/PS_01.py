input1 = int(input("Enter 1st number :: "))
input2 = int(input("Enter 2nd number :: "))
input3 = int(input("Enter 3rd number :: "))
input4 = int(input("Enter 4th number :: "))

max = input1

if(max < input2):
    max = input2

if(max < input3):
    max = input3

if(max < input4):
    max = input4

print("Maximum number is :: " + str(max))

# if(input1>input2 and input1>input3 and input1>input4):
# 