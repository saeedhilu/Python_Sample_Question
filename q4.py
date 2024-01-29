# Write a function to calculate the sum of all even numbers between 1 and n.
def fun1(n):
    sum = 0
    for i in range(1,n+1):
       if i % 2 ==0:
           sum +=i
    return sum

a = fun1(5)
print(a)
# Write a function to calculate the sum of all odd numbers between 1 and n.
def func1(n):
    sum = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            sum += i 
    return sum
b = func1(5)
print(b)