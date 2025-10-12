def maxThree(a , b , c):
    max = a
    if(b>max):
        max = b
    if(c>max):
        max = c
    return max

a = maxThree(0,5,-6)
print(a)