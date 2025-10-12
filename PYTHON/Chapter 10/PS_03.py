class Demo:
    a = 4

o = Demo()
print(o.a)    # Print the class attribute becqause instance attribute is not present 
o.a = 0       # Instance attribute is set 
print(o.a)    # Prints the instance attributs because instance attribute is present 
print(Demo.a) # class attribute don't change but instance attribute is set 