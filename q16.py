# Write a program to find the sum of all the multiples of 3 or 5 below a given number.
def functins(number):
    sum = 0
    for i in range(3,number+1):
        if i %  3 ==0 or  i % 5 ==0:
            sum += i
    return sum
value = functins(6)
print(value)
# 
def functions(vlaue):
    return sum(i for i in range(3, value) if value % 3 == 0 or value % 5 ==0)
print(functins(6))