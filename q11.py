# Write a function to calculate the factorial of a given number              n
def factorial(n):
    if n ==1 or n==0:
        return 1
    sum= 1
    for i in range(1,n+1):
        sum*=i
    return sum
value = factorial(3)
print(value)
# another methiod using recursion
def factorial(n):
    if n == 0 or n==1:
        return 1
    for i in range(1, n+1):
        sum = n * factorial(n-1)
    return sum
value = int(input("Enter the value"))
reslt = factorial(value)
print(reslt)
# 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

value = factorial(3)
print(value)
