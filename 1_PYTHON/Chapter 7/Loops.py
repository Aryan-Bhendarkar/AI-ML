
#  While loop 
i = 0
while(i<6):
    print(i)
    i = i+1
    
# Content of the List 
list = ["Harry" , 1, False, "This", "Rohan"]
i=0 
while(i<len(list)):
    print(list[i])
    i += 1

# For Loop range(start , end, step)
for j in range(0 , 6 , 2):
    print(j)

# For loop with list
for i in list:
    print(i)

tuple = (6, 231, 75, 122)

# For loop with Strings
name = "Harry"
for i in name:
    print(i)

# For Loop with else :: execute else when loop exhaust  
for i in list:
    print(i )
else:
    print("done")