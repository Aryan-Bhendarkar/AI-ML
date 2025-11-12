
l = ["Rohan" , "Harry" , "an"]
def removeNstrip(l ,  word):
    n = []
    for item in l:
        if (item != word):
            n.append(item.strip(word))
    return n
print(removeNstrip(l , "an"))