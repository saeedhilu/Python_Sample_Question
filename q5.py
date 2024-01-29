# Write a function to check if a given number is prime.
def fun(n):
    if n <=2:
       print("This is not possible")
    
    count = 0
    for i in range(2,n):
        if n % i ==0:
           count+=1
    return count==0
f = fun(8)
print(f)
# Write a function to check if a given number is prime.

def f1(m):
    return all(m % i !=0 for i in range(2,m))
print(f1(5))

# Write a function to check if a given number is prime.
def function2(n):
    if n<=2:
        return "This is not Possible"
    count = 0
    i = 2
    
    while i < n :
        if n % i ==0 :
            count+=1
        i+=1
    return count == 0
print(function2(7))
from sympy import isprime
number = 17
if isprime(number):
    print("Prime number")
else:
    print("none prime")
