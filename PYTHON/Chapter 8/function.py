a = 12
b = 45
c = 56

average = (a+b+c)/3
# print(average)

def avg():
    a = int(input("Enter the number1 :: "))
    b = int(input("Enter the number2 :: "))
    c = int(input("Enter the number3 :: "))

    average = (a+b+c)/3
    print(average)

# avg()c

def greet(name):
    print("Good day! "+ name )

# greet("Aryan")
# greet("Pagal")

def greet(name, ending):
    print("Good day! "+ name )
    print(ending)

# greet("Aryan" , "Thank you")
# greet("Pagal" , "Thanks")

def greet(name, ending):
    print("Good day! "+ name )
    print(ending)
    return name

a = greet("Aryan" , "Thank you")
print("return :: " + a)
greet("Pagal" , "Thanks")