str = "Hey Harry, You are amazing !!"
f = open("myFile.txt" , "w")
f.write(str)
f.close()

print(f.read())

#  Print all the Lines one-by-one
