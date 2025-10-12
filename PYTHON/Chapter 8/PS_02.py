def convertor(celsius):
    fahrenheit = (9/5) * celsius + 32 
    return fahrenheit

a = int(input("Enter the temp :: "))
print(f"Temperature in F :: {convertor(a)}")