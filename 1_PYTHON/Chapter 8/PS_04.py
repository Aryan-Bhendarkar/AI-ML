def findSum(n):
    if (n == 1):
        return 1
    return findSum(n-1) + n

a = int(input("Enter the number :: "))
print(f"Sum of n number:: {findSum(a)}")