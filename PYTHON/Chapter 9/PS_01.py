# checkTwinkle = False

# with open("Chapter 9\poems.txt" , "r") as f:
#     searchSpace = f.read()
#     if(searchSpace.find("twinkle") != -1):
#             checkTwinkle = True

# print(checkTwinkle)

f = open("Chapter 9\poems.txt")
content = f.read()
if('twinkle' in content):
    print("It is present ")
else:
    print("Not Present")

f.close()